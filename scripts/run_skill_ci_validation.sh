#!/usr/bin/env bash
set -euo pipefail

mode="${SKILL_VALIDATION_MODE:?SKILL_VALIDATION_MODE is required}"
targets="${SKILL_VALIDATION_TARGETS:-}"

if [[ "$mode" == "full" ]]; then
  bash scripts/validate_skills.sh
  exit 0
fi

if [[ "$mode" != "focused" ]]; then
  printf 'error: unsupported skill validation mode: %s\n' "$mode" >&2
  exit 1
fi

read -r -a skills <<< "$targets"

if ((${#skills[@]} == 0)); then
  printf 'error: focused validation mode requires at least one skill target\n' >&2
  exit 1
fi

bash scripts/validate_skills.sh "${skills[@]}"
