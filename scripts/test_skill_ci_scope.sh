#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

source scripts/skill_ci_scope.sh

assert_scope() {
  local expected="$1"
  shift
  local actual

  actual="$(classify_changed_files "$@")"
  if [[ "$actual" != "$expected" ]]; then
    printf 'expected scope:\n%s\nactual scope:\n%s\n' "$expected" "$actual" >&2
    return 1
  fi
}

assert_scope $'mode=focused\nskills=oiticica-style oiticica-style-defects' \
  scripts/generate_skills.py \
  src/oiticica-style/SKILL.md \
  src/oiticica-style/evals/evals.yaml \
  src/oiticica-style-defects/SKILL.md
assert_scope 'mode=skip' scripts/generate_skills.py
assert_scope 'mode=skip' scripts/link_skills.sh README.md
assert_scope 'mode=full' scripts/validate_skills.sh
assert_scope 'mode=full' scripts/skilpel.yaml src/oiticica-style/SKILL.md
assert_scope 'mode=full' .github/workflows/skill-ci.yml

echo 'skill CI scope tests passed'
