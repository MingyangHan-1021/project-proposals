"""Validate DSAN 6725 final project proposals.

Checks every markdown file under proposals/ for the required sections, a valid team
roster, a one line title, and an abstract within the word limit. The same check runs
on every pull request, so run it locally before you open one:

    uv run python scripts/validate_proposals.py
"""

import argparse
import logging
import re
import sys
from pathlib import Path

# Configure logging with basicConfig
logging.basicConfig(
    level=logging.INFO,  # Set the log level to INFO
    # Define log message format
    format="%(asctime)s,p%(process)s,{%(filename)s:%(lineno)d},%(levelname)s,%(message)s",
)

logger = logging.getLogger(__name__)

PROPOSALS_DIR: str = "proposals"
FILENAME_PATTERN: str = r"^team-\d{2}\.md$"
SKIPPED_FILES: tuple = ("README.md",)

SECTION_TEAM_NUMBER: str = "Team Number"
SECTION_TEAM_NAME: str = "Team Name"
SECTION_TEAM_MEMBERS: str = "Team Members"
SECTION_TITLE: str = "Project Title"
SECTION_ABSTRACT: str = "Abstract"

REQUIRED_SECTIONS: tuple = (
    SECTION_TEAM_NUMBER,
    SECTION_TEAM_NAME,
    SECTION_TEAM_MEMBERS,
    SECTION_TITLE,
    SECTION_ABSTRACT,
)

MIN_ABSTRACT_WORDS: int = 150
MAX_ABSTRACT_WORDS: int = 300
MIN_TEAM_SIZE: int = 2
MAX_TEAM_SIZE: int = 4
PLACEHOLDER_MARKERS: tuple = ("TODO", "FIXME", "your name", "your netid")


def _strip_html_comments(
    text: str
) -> str:
    """Remove HTML comments so template instructions do not count as content."""
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def _split_into_sections(
    text: str
) -> dict[str, str]:
    """Split markdown into a mapping of level two heading to its body text."""
    sections: dict[str, str] = {}
    current_heading = None
    current_lines: list[str] = []

    for line in text.splitlines():
        if line.startswith("## "):
            if current_heading is not None:
                sections[current_heading] = "\n".join(current_lines).strip()
            current_heading = line[3:].strip()
            current_lines = []
        elif current_heading is not None:
            current_lines.append(line)

    if current_heading is not None:
        sections[current_heading] = "\n".join(current_lines).strip()

    logger.debug(f"Found sections: {list(sections.keys())}")
    return sections


def _parse_members_table(
    body: str
) -> list[list[str]]:
    """Return the data rows of a markdown table as lists of cell values."""
    separator_characters = set("-: ")
    rows: list[list[str]] = []

    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue

        cells = [cell.strip() for cell in line.strip("|").split("|")]

        is_separator = all(
            cell != "" and set(cell) <= separator_characters for cell in cells
        )
        is_header = cells[0].lower() == "name"
        if is_separator or is_header:
            continue

        rows.append(cells)

    return rows


def _check_filename(
    path: Path
) -> list[str]:
    """Check that the file is named team-NN.md."""
    if re.match(FILENAME_PATTERN, path.name):
        return []

    message = (
        f"Filename '{path.name}' is not valid. Use 'team-NN.md' with a two digit "
        f"team number, for example 'team-07.md'."
    )
    return [message]


def _check_missing_sections(
    sections: dict[str, str]
) -> list[str]:
    """Check that every required heading is present."""
    return [
        f"Section '## {name}' is missing. Copy the headings from TEMPLATE.md exactly."
        for name in REQUIRED_SECTIONS
        if name not in sections
    ]


def _check_team_number(
    sections: dict[str, str],
    path: Path
) -> list[str]:
    """Check that the team number is a number and matches the filename."""
    body = sections.get(SECTION_TEAM_NUMBER, "")
    if not body:
        return [f"Section '{SECTION_TEAM_NUMBER}' is empty."]

    if not body.isdigit():
        return [f"Team number '{body}' is not a number. Use digits only, like 07."]

    digits_in_filename = re.search(r"\d{2}", path.name)
    if digits_in_filename and int(body) != int(digits_in_filename.group()):
        message = (
            f"Team number '{body}' does not match the filename '{path.name}'. "
            f"Rename the file or fix the team number so the two agree."
        )
        return [message]

    return []


def _check_team_name(
    sections: dict[str, str]
) -> list[str]:
    """Check that the team name is filled in."""
    if not sections.get(SECTION_TEAM_NAME, ""):
        return [f"Section '{SECTION_TEAM_NAME}' is empty."]

    return []


def _check_members(
    sections: dict[str, str]
) -> list[str]:
    """Check the roster table for team size and a name plus NetID per member."""
    rows = _parse_members_table(sections.get(SECTION_TEAM_MEMBERS, ""))
    if not rows:
        message = (
            f"Section '{SECTION_TEAM_MEMBERS}' has no member rows. Keep the table "
            f"from TEMPLATE.md and add one row per member."
        )
        return [message]

    errors: list[str] = []
    if len(rows) < MIN_TEAM_SIZE or len(rows) > MAX_TEAM_SIZE:
        errors.append(
            f"Found {len(rows)} member rows. Teams must have between "
            f"{MIN_TEAM_SIZE} and {MAX_TEAM_SIZE} members."
        )

    for row_number, cells in enumerate(rows, start=1):
        if len(cells) < 2:
            errors.append(f"Member row {row_number} needs both a name and a NetID.")
            continue
        if not cells[0]:
            errors.append(f"Member row {row_number} is missing a name.")
        if not cells[1]:
            errors.append(f"Member row {row_number} is missing a NetID.")

    return errors


def _check_title(
    sections: dict[str, str]
) -> list[str]:
    """Check that the title is present and fits on one line."""
    body = sections.get(SECTION_TITLE, "")
    if not body:
        return [f"Section '{SECTION_TITLE}' is empty."]

    if len(body.splitlines()) > 1:
        return [f"Section '{SECTION_TITLE}' must be a single line."]

    return []


def _check_abstract(
    sections: dict[str, str]
) -> list[str]:
    """Check that the abstract is present and within the word limits."""
    body = sections.get(SECTION_ABSTRACT, "")
    word_count = len(body.split())
    logger.debug(f"Abstract word count: {word_count}")

    if word_count == 0:
        return [f"Section '{SECTION_ABSTRACT}' is empty."]

    if word_count > MAX_ABSTRACT_WORDS:
        message = (
            f"Abstract is {word_count} words. The limit is {MAX_ABSTRACT_WORDS} "
            f"words, so cut {word_count - MAX_ABSTRACT_WORDS}."
        )
        return [message]

    if word_count < MIN_ABSTRACT_WORDS:
        message = (
            f"Abstract is only {word_count} words. Write at least "
            f"{MIN_ABSTRACT_WORDS} words, and aim for 250 to 300."
        )
        return [message]

    return []


def _check_placeholders(
    text: str
) -> list[str]:
    """Check that no template placeholder text was left behind."""
    lowered = text.lower()

    return [
        f"Placeholder text '{marker}' is still in the file."
        for marker in PLACEHOLDER_MARKERS
        if marker.lower() in lowered
    ]


def _validate_file(
    path: Path
) -> list[str]:
    """Return every validation error found in a single proposal file.

    Structural problems, a bad filename or a missing heading, are reported on their
    own. The content checks only run once the structure is correct, because their
    messages are confusing otherwise.
    """
    text = _strip_html_comments(path.read_text(encoding="utf-8"))
    sections = _split_into_sections(text)

    structural_errors = _check_filename(path) + _check_missing_sections(sections)
    if structural_errors:
        return structural_errors

    return (
        _check_team_number(sections, path)
        + _check_team_name(sections)
        + _check_members(sections)
        + _check_title(sections)
        + _check_abstract(sections)
        + _check_placeholders(text)
    )


def _print_report(
    results: dict[str, list[str]]
) -> None:
    """Log one line per passing file and one block per failing file."""
    for filename in sorted(results):
        errors = results[filename]
        if not errors:
            logger.info(f"PASS {filename}")
            continue

        logger.error(f"FAIL {filename}")
        for error in errors:
            logger.error(f"       {error}")


def _build_argument_parser() -> argparse.ArgumentParser:
    """Build the command line parser."""
    parser = argparse.ArgumentParser(
        description="Validate DSAN 6725 final project proposals.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage:
    # Validate every proposal in proposals/
    uv run python scripts/validate_proposals.py

    # Validate another directory, with debug logging
    uv run python scripts/validate_proposals.py --proposals-dir drafts --debug
""",
    )
    parser.add_argument(
        "--proposals-dir",
        default=PROPOSALS_DIR,
        help=f"Directory holding the proposal files (default: {PROPOSALS_DIR})",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Set the log level to DEBUG",
    )
    return parser


def validate_proposals(
    proposals_dir: Path
) -> dict[str, list[str]]:
    """Validate every proposal file in a directory.

    Args:
        proposals_dir: Directory holding the team proposal markdown files.

    Returns:
        Mapping of filename to the list of errors found in that file. An empty list
        means the file passed.

    Raises:
        FileNotFoundError: If the directory does not exist.

    Example:
        >>> results = validate_proposals(Path("proposals"))
        >>> results["team-00.md"]
        []
    """
    if not proposals_dir.is_dir():
        raise FileNotFoundError(
            f"Directory not found: {proposals_dir}. Run this from the repository root."
        )

    results: dict[str, list[str]] = {}
    for path in sorted(proposals_dir.glob("*.md")):
        if path.name in SKIPPED_FILES:
            logger.debug(f"Skipping {path.name}")
            continue

        logger.debug(f"Validating {path}")
        results[path.name] = _validate_file(path)

    return results


def main() -> int:
    """Validate all proposals and return a shell exit code."""
    args = _build_argument_parser().parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    results = validate_proposals(Path(args.proposals_dir))
    _print_report(results)

    failed = [name for name, errors in results.items() if errors]
    if failed:
        logger.error(
            f"{len(failed)} of {len(results)} proposal files have errors. "
            f"Fix the items listed above and push again."
        )
        return 1

    logger.info(f"All {len(results)} proposal files passed validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
