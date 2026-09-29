# DSAN 6725 Final Project Proposals

Applied Generative AI for AI Developers, Fall 2026. Georgetown University.

Every team submits a final project proposal here as a pull request. The proposal is
your project title and abstract. The professor approves it before you start building.

**Due: Tuesday, October 6, 2026.**

## Overview

DSAN 6725 is an applied AI course. Your final project is production-quality software
that solves a real problem. Every project must implement AI agents unless the
professor approves another approach.

The proposal is the first gate. Write it so the professor can tell you two things:
whether the scope fits six weeks, and whether the architecture holds up. Vague
proposals come back with change requests.

For project ideas and the full list of final deliverables, see the
[DSAN 6725 Final Project](https://github.com/gu-dsan6725/spring-2026-georgetown-university-dsan6725-applied-genai-for-ai-developers-spring-2026-final-project)
repository.

## What to submit

One markdown file, `proposals/team-NN.md`, where `NN` is your two digit project group
number. Copy [TEMPLATE.md](TEMPLATE.md) and fill in five sections.

| Section | What goes in it |
| ------- | --------------- |
| Team Number | Your project group number, digits only |
| Team Name | A short name for your team |
| Team Members | Full name and NetID for each member, 2 to 4 members |
| Project Title | One line, specific about what you are building |
| Abstract | 250 to 300 words, and no more than 300 |

List every member in the file. One member opens the pull request for the team.

[proposals/team-00.md](proposals/team-00.md) is a worked example. Read it before you
start, then pick your own project idea.

## What the abstract must cover

Five things, inside 300 words. If you cannot explain the project in 300 words, you do
not yet know what you are building.

1. **The problem.** What breaks today, who it hurts, and why it matters.
2. **The architecture.** Your agents, what each one does, and how they coordinate.
3. **The data and tools.** Name the data sources, APIs, and services, and confirm you
   can reach them.
4. **The evaluation.** Name the metrics. Say what counts as working.
5. **The biggest risk.** The one thing most likely to stop you finishing in six
   weeks, and your plan for it.

Most weak proposals fail on 3 and 5. A proposal comes back when the data source turns
out to be unreachable, or when a risk sits in the middle of the design and nobody
names it.

## How to submit

### Option A: in the browser

Use this if you want to add one file and set nothing up.

1. Open [TEMPLATE.md](TEMPLATE.md) and copy the whole file.
2. Go to the [proposals](proposals) folder, click **Add file**, then **Create new
   file**.
3. Name the file `team-NN.md` with your two digit team number. GitHub offers to fork
   the repository. Accept.
4. Paste the template, fill it in, and click **Propose new file**.
5. Open the pull request and work through the checklist in the description.

### Option B: on the command line

Use this if you want to run the check before you submit.

```bash
# Fork and clone. Team 07 is the example throughout.
gh repo fork gu-dsan6725/project-proposals --clone
cd project-proposals

# Work on a branch
git checkout -b team-07-proposal

# Start from the template
cp TEMPLATE.md proposals/team-07.md

# Edit proposals/team-07.md, then check it
uv run python scripts/validate_proposals.py

# Submit
git add proposals/team-07.md
git commit -m "Add project proposal for team 07"
git push origin team-07-proposal
gh pr create --title "Team 07 project proposal" --fill
```

Install `uv` first if you do not have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
```

## What the automated check covers

A GitHub Action runs on every pull request and checks the mechanics, so review time
goes to your idea. It reports on:

- Filename is `team-NN.md` with a two digit team number
- The team number inside the file matches the filename
- All five sections appear, with the headings from the template
- The roster lists 2 to 4 members, each with a name and a NetID
- The title fits on one line
- The abstract runs 150 to 300 words
- The template placeholder text is gone

If the check goes red, fix what it lists and push to the same branch. The pull request
updates itself, so do not open a second one. A green check only means the mechanics
are right. It says nothing about your idea.

Run the same check yourself at any time:

```bash
uv run python scripts/validate_proposals.py
```

## After you submit

The professor and TAs read your proposal, then merge it or request changes. A merge
means you can start building. If they request changes, push an update to the same
branch and ask for another review. Hold off on serious building until your proposal
merges.

## FAQ

**Can I submit alone, or with more than four people?**
No. Teams run 2 to 4 members.

**Which team number do I use?**
Your project group number, the same one as your `Project Group N` team in the
`gu-dsan6725` organization. Ask on Slack if you do not know yours.

**Does every member open a pull request?**
No. One pull request per team, from any one member. List everybody inside the file.

**Can I use any model provider?**
Yes. Use whatever works best for your project.

**We want to change the project after approval.**
Small changes to the architecture or the data need no approval. Talk to the professor
before you change the problem statement, then update your file in a new pull request.

**My abstract runs 310 words and I cannot cut it.**
You can. The cuts hide in your first two sentences, where you explain background the
reader already has.

**Is 150 words a target?**
No. It is a floor that catches stubs. Aim for 250 to 300.

**Can I read other teams' proposals?**
Yes. This repository is public, and merged proposals are visible to everybody.
Copying from them breaks the [honor code](https://honorcouncil.georgetown.edu/).

**What is the late policy?**
The proposal counts as a project intermediate assignment. The syllabus late policy
for those applies.

## Repository layout

```text
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
        └── validate-proposals.yml      # runs the check
```
