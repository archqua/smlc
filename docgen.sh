#!/usr/bin/env bash
COMMIT_MSG=${1:-synchronizing docs}
pdoc -t pdoc_template -o docs smlc &&
git add -A &&
echo git commit -m \"$COMMIT_MSG\" &&
git commit -m "$COMMIT_MSG"
repeat_commit=$?
if (( repeat_commit != 0 )); then
  echo repeat commit 1/3 \(trailing whitespace\) &&
  git add -A &&
  echo git commit -m \"$COMMIT_MSG\" &&
  git commit -m "$COMMIT_MSG"
  repeat_commit=$?
fi
if (( repeat_commit != 0 )); then
  echo repeat commit 2/3 \(black\) &&
  git add -A &&
  echo git commit -m \"$COMMIT_MSG\" &&
  git commit -m "$COMMIT_MSG"
  repeat_commit=$?
fi
if (( repeat_commit != 0 )); then
  echo repeat commit 3/3 \(docformatter\) &&
  git add -A &&
  echo git commit -m \"$COMMIT_MSG\" &&
  git commit -m "$COMMIT_MSG"
  repeat_commit=$?
fi
