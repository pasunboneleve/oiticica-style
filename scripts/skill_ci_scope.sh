#!/usr/bin/env bash
set -euo pipefail

is_zero_sha() {
  [[ "$1" =~ ^0+$ ]]
}

changed_files_for_event() {
  local event_name="$1"
  local head_sha="$2"
  local base_sha="$3"
  local before_sha="$4"

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

classify_changed_files() {
  local path
  local skill
  local -a changed_files=("$@")
  local -a skills=()
  local -A seen_skills=()

  if ((${#changed_files[@]} == 0)); then
    echo "mode=skip"
    return
  fi

  for path in "${changed_files[@]}"; do
    case "$path" in
      .github/workflows/skill-ci.yml|scripts/skill_ci_scope.sh|scripts/run_skill_ci_validation.sh|scripts/validate_skills.sh|scripts/skilpel.yaml)
        echo "mode=full"
        return
        ;;
    esac
  done

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
    return
  fi

  echo "mode=focused"
  printf 'skills=%s\n' "${skills[*]}"
}

main() {
  local event_name="${1:?event name is required}"
  local head_sha="${2:?head SHA is required}"
  local base_sha="${3:-}"
  local before_sha="${4:-}"
  local -a changed_files=()

  if [[ "$event_name" != "pull_request" && "$event_name" != "push" ]]; then
    echo "mode=full"
    return
  fi

  mapfile -t changed_files < <(changed_files_for_event "$event_name" "$head_sha" "$base_sha" "$before_sha")
  classify_changed_files "${changed_files[@]}"
}

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
  main "$@"
fi
