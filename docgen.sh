#!/usr/bin/env bash
COMMIT_MSG=${1:-synchronizing docs}
pdoc -t pdoc_template -o docs smlc && (
  pre-commit run --files docs/smlc/*
  git add -A &&
  git commit -m "$COMMIT_MSG"
)
