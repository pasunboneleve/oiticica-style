#!/usr/bin/env bash
set -euo pipefail

event_name="${1:?event name is required}"
head_sha="${2:?head SHA is required}"
base_sha="${3:-}"
before_sha="${4:-}"

if [[ "$event_name" != "pull_request" && "$event_name" != "push" ]]; then
  echo "mode=full"
  exit 0
fi

is_zero_sha() {
  [[ "$1" =~ ^0+$ ]]
}

changed_files_for_event() {
  case "$event_name" in
    pull_request)
      git diff --name-only "$base_sha" "$head_sha"
      ;;
    push)
      if [[ -z "$before_sha" ]] || is_zero_sha "$before_sha"; then
        git diff-tree --no-commit-id --name-only -r "$head_sha"
      else
        git diff --name-only "$before_sha" "$head_sha"
      fi
      ;;
  esac
}

mapfile -t changed_files < <(changed_files_for_event)

if ((${#changed_files[@]} == 0)); then
  echo "mode=skip"
  exit 0
fi

for path in "${changed_files[@]}"; do
  case "$path" in
    .github/workflows/skill-ci.yml|scripts/*)
      echo "mode=full"
      exit 0
      ;;
  esac
done

declare -A seen_skills=()
skills=()

for path in "${changed_files[@]}"; do
  case "$path" in
    src/*/*)
      skill="${path#src/}"
      skill="${skill%%/*}"
      if [[ -f "src/$skill/SKILL.md" && -z "${seen_skills[$skill]+x}" ]]; then
        seen_skills["$skill"]=1
        skills+=("$skill")
      fi
      ;;
  esac
done

if ((${#skills[@]} == 0)); then
  echo "mode=skip"
  exit 0
fi

echo "mode=focused"
printf 'skills=%s\n' "${skills[*]}"
