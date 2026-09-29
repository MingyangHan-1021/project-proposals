# DSAN 6725 Final Project Proposal

<!--
A worked example, not a submission. It shows the level of detail a proposal needs, and
CI validates it alongside the real ones, which proves the rules are satisfiable. Do
not edit this file, and pick your own project idea.
-->

## Team Number

00

## Team Name

Example Team

## Team Members

| Name        | NetID  |
| ----------- | ------ |
| Alex Rivera | ar0001 |
| Priya Menon | pm0002 |
| Sam Okonkwo | so0003 |

## Project Title

CI Triage Agent: classifying continuous integration failures and recommending the next action

## Abstract

Continuous integration pipelines fail for reasons that have nothing to do with the
code under review: a flaky test, an expired credential, a network timeout. They also
fail because of real regressions, and telling those cases apart takes a human reading
the log. Engineers at mid-size companies spend hours a week doing that, and the cost
climbs with every test they add.

We will build CI Triage Agent, a multi-agent system that reads a failed pipeline run
and returns a labeled diagnosis with a recommended action. Four agents divide the
work. The retrieval agent pulls the failing job log, the diff under test, and the last
thirty runs of the same job from the CI provider API. A classifier then labels the
failure as flaky, infrastructure, dependency, or regression, citing the log lines
behind its label. To catch flakiness, a third agent looks for the same test failing on
unrelated commits. The reporting agent drafts a pull request comment, and for
infrastructure failures it adds the retry command.

Our data is the public GitHub Actions logs of three large open source repositories,
roughly four thousand failed runs. We will hand label six hundred as a held-out test
set. We measure per-class accuracy, median cost per triage in tokens and dollars, and
above all the false regression rate, because a missed regression is the expensive
mistake. A single-prompt baseline runs against the same test set, which shows whether
four agents earn their cost.

The risk is log volume, since one run can exceed the model context window. We will
index each log and hand the classifier only the failing region.
