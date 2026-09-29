# AGENTS.md

Instructions for AI coding agents working in this repository (DSAN 6725, Applied
Generative AI for AI Developers, Fall 2026). Human contributors: start with
`README.md`.

Students point coding agents at this repo to draft a proposal. Read this first, and
follow the same rules a student follows.

## What this repo is

A submission repo. Each team adds one markdown file and opens a pull request. There is
no application to ship.

- `proposals/team-NN.md` is one team's proposal. `NN` is a two digit project group
  number.
- `TEMPLATE.md` is what a team copies to start.
- `proposals/team-00.md` is a worked example. CI validates it alongside real
  submissions, so it has to keep passing.
- `scripts/validate_proposals.py` is the check that runs on every pull request.

## Dev environment

Python >=3.11, managed with `uv`. The validator uses the standard library only, so
there is nothing to install.

## Commands

- **Validate every proposal:** `uv run python scripts/validate_proposals.py`
- **Validate with tracing:** add `--debug` to see the parsed sections and the abstract
  word count
- **Compile check:** `uv run python -m py_compile scripts/validate_proposals.py`
- **Lint:** `uvx ruff check scripts/`

Run the validator before you commit. It is the same code that gates the pull request,
so a green local run means a green check.

## Writing a proposal

Copy `TEMPLATE.md` to `proposals/team-NN.md` and fill in all five sections. The
validator enforces the mechanics:

| Rule | Detail |
| ---- | ------ |
| Filename | `team-NN.md`, two digits, and the team number inside the file matches |
| Sections | All five headings from the template, spelled the same way |
| Roster | 2 to 4 rows, each with a name and a NetID |
| Title | One line |
| Abstract | 150 to 300 words |
| Placeholders | No `TODO`, `FIXME`, `your name`, or `your netid` left behind |

The abstract has to cover the problem, the agent architecture, the data sources and
tools, the evaluation plan, and the biggest risk. Read `proposals/team-00.md` for the
level of detail, and write about the team's own project.

The word limit is the hard part. Draft long, then cut. The cuts are almost always in
the opening background sentences.

## Rules

- Touch one file per pull request, the team's own proposal. Leave other teams' files
  alone.
- Never edit `scripts/validate_proposals.py` to make a proposal pass. Fix the proposal.
- Never edit `proposals/team-00.md`. It is the example.
- Do not invent team members, NetIDs, or a team number. Ask the student for them.
- Do not invent data sources or results. A proposal naming a dataset nobody can reach
  comes straight back in review.

## Code style

Applies when changing `scripts/validate_proposals.py`.

- `uv` for packages, never `pip`.
- Private functions start with `_` and sit at the top of the file, public ones below.
- One parameter per line, with type annotations. Builtin generics (`list`, `dict`), not
  `typing.List`.
- Two blank lines between functions. Functions under 50 lines.
- `main()` parses arguments and delegates. No business logic in it.
- Standard logging config, the one already at the top of the script. Keep CI on the
  standard library.
- No emojis anywhere. No em-dashes in prose, use a comma, a colon, or two sentences.

## Prose style

The course writing style applies to every markdown file here. Active voice. Short
words. Cut the padding. No stock phrases, no `-ly` adverbs where a stronger verb works,
no defining something by saying what it is not, and no two sentences in a paragraph
sharing the same shape.
