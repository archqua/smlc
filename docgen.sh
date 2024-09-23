#!/usr/bin/env bash
COMMIT_MSG=${1:-synchronizing docs}
pdoc -t pdoc_template -o docs smlc && (
pre-commit run --files docs/smlc/*
git add -A &&
git commit -m "$COMMIT_MSG"
)
# repeat_commit=$?
# if (( repeat_commit != 0 )); then
#   echo repeat commit \(trailing whitespace\) &&
#   git add -A &&
#   git commit -m "$COMMIT_MSG"
#   repeat_commit=$?
# fi
# if (( repeat_commit != 0 )); then
#   echo repeat commit 2/3 \(black\) &&
#   git add -A &&
#   git commit -m "$COMMIT_MSG"
#   repeat_commit=$?
# fi
# if (( repeat_commit != 0 )); then
#   echo repeat commit 3/3 \(docformatter\) &&
#   git add -A &&
#   git commit -m "$COMMIT_MSG"
#   repeat_commit=$?
# fi
