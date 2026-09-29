# DSAN 6725 Final Project Proposals

Applied Generative AI for AI Developers, Fall 2026. Georgetown University.

Every team submits its final project proposal to this repository as a pull request.
The proposal is your project title and abstract, and it is the checkpoint where the
scope and direction of your project get approved before you start building.

**Due: Tuesday, October 6, 2026.**

## Overview

DSAN 6725 is an applied AI course. The final project is production-quality software
that solves a real problem, not a toy demo. All projects must implement AI agents
unless an alternative approach is explicitly approved by the professor.

This proposal is the first gate. A good one is specific enough that the professor can
tell you whether the scope is right for six weeks, and whether the architecture makes
sense. A vague proposal will come back with change requests, which costs you time.

For project ideas and the full list of final deliverables, see the
[DSAN 6725 Final Project](https://github.com/gu-dsan6725/spring-2026-georgetown-university-dsan6725-applied-genai-for-ai-developers-spring-2026-final-project)
repository.

## What to submit

One markdown file, `proposals/team-NN.md`, where `NN` is your two digit project group
number. Copy [TEMPLATE.md](TEMPLATE.md) and fill in five things:

| Section | What goes in it |
|---------|-----------------|
| Team Number | Your project group number, digits only |
| Team Name | A short name for your team |
| Team Members | Full name and NetID for each member, 2 to 4 members |
| Project Title | One line, specific about what you are building |
| Abstract | 250 to 300 words, and not more than 300 |

Any one member submits the pull request on behalf of the whole team. Everybody must
be listed in the file, but only one person opens the pull request.

[proposals/team-00.md](proposals/team-00.md) is a worked example. Read it before you
start. Do not reuse that project idea.

## What the abstract must cover

Five things, inside the 300 word limit. The limit is the point: if you cannot explain
the project in 300 words, the scope is not yet clear enough to build.

1. **The problem.** What is broken today, who suffers from it, and why it matters.
2. **The architecture.** What your agents are, what each one is responsible for, and
   how they coordinate.
3. **The data and tools.** Which data sources, APIs, and external services you will
   use. Name them, and confirm you can actually access them.
4. **The evaluation.** How you will know the system works, and what you will measure.
   Name the metrics.
5. **The biggest risk.** The one thing most likely to stop you finishing in six weeks,
   and your plan for handling it.

Points 3 and 5 are where most weak proposals fall down. A project with no reachable
data source, or with an unacknowledged risk sitting in the middle of it, is the most
common reason a proposal gets sent back.

## How to submit

### Option A: in the browser

Good if you only want to add one file and do not want to set anything up.

1. Open [TEMPLATE.md](TEMPLATE.md) and copy the whole file.
2. Go to the [proposals](proposals) folder, click **Add file**, then **Create new
   file**.
3. Name the file `team-NN.md`, using your two digit team number. GitHub will offer to
   fork the repository for you. Accept.
4. Paste the template, fill it in, and click **Propose new file**.
5. Open the pull request and complete the checklist in the description.

### Option B: on the command line

Good if you want to run the validator locally before you submit.

```bash
# Fork and clone, using team 07 as the example throughout
gh repo fork gu-dsan6725/project-proposals --clone
cd project-proposals

# Work on a branch
git checkout -b team-07-proposal

# Start from the template
cp TEMPLATE.md proposals/team-07.md

# Edit proposals/team-07.md, then check it before you push
uv run python scripts/validate_proposals.py

# Submit
git add proposals/team-07.md
git commit -m "Add project proposal for team 07"
git push origin team-07-proposal
gh pr create --title "Team 07 project proposal" --fill
```

If you do not have `uv` yet:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
```

## What gets checked automatically

A GitHub Action runs on every pull request and checks the things that are mechanical,
so that review time goes to the substance of your idea instead. It reports:

- The file is named `team-NN.md` with a two digit team number
- The team number inside the file matches the filename
- All five required sections are present, with the exact headings from the template
- The roster has 2 to 4 members, each with a name and a NetID
- The title is a single line
- The abstract is at least 150 words and no more than 300
- No template placeholder text was left behind

A red check means fix it and push again to the same branch. The pull request updates
itself, you do not need to open a new one. A green check means the mechanics are
fine, it says nothing about whether the idea is any good.

Run the same check locally at any time:

```bash
uv run python scripts/validate_proposals.py
```

## What happens after you submit

The professor and TAs review the proposal and either approve it or request changes.
Merged pull request means approved, and you can start building. Requested changes
means push an update to the same branch and re-request review. Do not start building
in earnest until your proposal is merged.

## FAQ

**Can I submit alone, or with more than four people?**
No. Teams must have 2 to 4 members.

**Which team number do I use?**
Your project group number, the same one as your `Project Group N` team in the
`gu-dsan6725` organization. Ask on Slack if you are not sure which one is yours.

**Do all team members need to open a pull request?**
No. One pull request per team, opened by any one member. Everybody is listed inside
the file.

**Can I use any model provider?**
Yes. Use whatever works best for your project.

**What if we change the project after the proposal is approved?**
Small changes to the architecture or the data are expected and fine. A different
problem statement is not. Talk to the professor first, then open a pull request that
updates your existing file.

**My abstract is 310 words and I cannot cut it.**
You can. The cuts are usually in the first two sentences of background that the
reader already knows.

**Is the 150 word floor a target?**
No, it is a floor to catch stubs. Aim for 250 to 300.

**Can I see other teams' proposals?**
Yes, this repository is public and merged proposals are visible to everybody. Reading
them is fine, copying from them is not. The
[academic integrity policy](https://honorcouncil.georgetown.edu/) applies.

**What is the late policy?**
The proposal is a project intermediate assignment, so the late policy in the syllabus
for those applies.

## Repository layout

```
.
├── README.md                          # this file
├── TEMPLATE.md                        # copy this to start your proposal
├── proposals/
│   ├── team-00.md                     # worked example
│   └── team-NN.md                     # one file per team, you add yours
├── scripts/
│   └── validate_proposals.py          # the check that runs on every pull request
└── .github/
    ├── pull_request_template.md        # the submission checklist
    └── workflows/
        └── validate-proposals.yml      # runs the validator
```

## Questions

Ask on the course Slack. Per the syllabus, proposal questions are answered up to 12
hours before the deadline.
