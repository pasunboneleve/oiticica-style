#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_ROOT="${SKILLS_ROOT:-$ROOT/src}"
INSTALL_ROOT="${INSTALL_ROOT:-$HOME/.local}"
SKILL_VALIDATOR_VERSION="${SKILL_VALIDATOR_VERSION:-latest}"
AGENT_SKILLS_EVAL_VERSION="${AGENT_SKILLS_EVAL_VERSION:-latest}"
AGENT_SKILLS_EVAL_API_KEY_ENV="${AGENT_SKILLS_EVAL_API_KEY_ENV:-OPENAI_API_KEY}"
AGENT_SKILLS_EVAL_BASE_URL="${AGENT_SKILLS_EVAL_BASE_URL:-https://api.openai.com/v1}"
AGENT_SKILLS_EVAL_TARGET="${AGENT_SKILLS_EVAL_TARGET:-gpt-4o-mini}"
AGENT_SKILLS_EVAL_JUDGE="${AGENT_SKILLS_EVAL_JUDGE:-$AGENT_SKILLS_EVAL_TARGET}"
AGENT_SKILLS_EVAL_WORKSPACE="${AGENT_SKILLS_EVAL_WORKSPACE:-${TMPDIR:-/tmp}/agent-skills-eval-oiticica-style}"
AGENT_SKILLS_EVAL_MIN_PASS="${AGENT_SKILLS_EVAL_MIN_PASS:-0.90}"
AGENT_SKILLS_EVAL_MIN_DELTA="${AGENT_SKILLS_EVAL_MIN_DELTA:-0.20}"
export PATH="$INSTALL_ROOT/bin:$HOME/go/bin:$PATH"

usage() {
  printf 'usage: %s [skill-relpath ...]\n' "${0##*/}"
}

ensure_skill_validator() {
  if command -v skill-validator >/dev/null 2>&1; then
    return 0
  fi

  if ! command -v go >/dev/null 2>&1; then
    printf 'error: skill-validator is not in PATH and go is unavailable to install it\n' >&2
    return 1
  fi

  mkdir -p "$INSTALL_ROOT/bin"
  GOBIN="$INSTALL_ROOT/bin" go install "github.com/agent-ecosystem/skill-validator/cmd/skill-validator@$SKILL_VALIDATOR_VERSION"
}

ensure_eval_validator() {
  if command -v agent-skills-eval >/dev/null 2>&1; then
    return 0
  fi

  if command -v bun >/dev/null 2>&1; then
    bun add -g "agent-skills-eval@$AGENT_SKILLS_EVAL_VERSION"
    return $?
  fi

  if command -v npm >/dev/null 2>&1; then
    npm install -g "agent-skills-eval@$AGENT_SKILLS_EVAL_VERSION"
    return $?
  fi

  printf 'error: agent-skills-eval is not in PATH and neither bun nor npm is available to install it\n' >&2
  return 1
}

validate_skill_args() {
  local skill

  for skill in "$@"; do
    if [[ "$skill" == -* ]]; then
      usage >&2
      return 1
    fi

    if [[ ! -f "$SKILLS_ROOT/$skill/SKILL.md" ]]; then
      printf 'error: skill not found or missing SKILL.md: %s\n' "$skill" >&2
      return 1
    fi
  done
}

run_eval_validator() {
  local eval_status=0
  local run_workspace
  local skill
  local include_args=()

  for skill in "$@"; do
    include_args+=(--include "$skill")
  done

  run_workspace="$(mktemp -d "${AGENT_SKILLS_EVAL_WORKSPACE%/}.XXXXXX")" || return $?

  agent-skills-eval \
    --config "$ROOT/scripts/agent-skills-eval.yaml" \
    "$SKILLS_ROOT" \
    "${include_args[@]}" \
    --workspace "$run_workspace" \
    --baseline \
    --target "$AGENT_SKILLS_EVAL_TARGET" \
    --judge "$AGENT_SKILLS_EVAL_JUDGE" \
    --base-url "$AGENT_SKILLS_EVAL_BASE_URL" \
    --api-key-env "$AGENT_SKILLS_EVAL_API_KEY_ENV" \
    --no-report || eval_status=$?

  if ((eval_status != 0)); then
    printf 'agent-skills-eval exited with status %d; checking configured aggregate gates\n' "$eval_status" >&2
  fi

  check_eval_deltas "$run_workspace"
}

check_eval_deltas() {
  local workspace="$1"
  local js_runtime

  if command -v node >/dev/null 2>&1; then
    js_runtime=node
  elif command -v bun >/dev/null 2>&1; then
    js_runtime=bun
  else
    printf 'error: neither node nor bun is available to check agent-skills-eval deltas\n' >&2
    return 1
  fi

  "$js_runtime" "$ROOT/scripts/check_eval_deltas.js" "$workspace" "$AGENT_SKILLS_EVAL_MIN_DELTA" "$AGENT_SKILLS_EVAL_MIN_PASS"
}

run_skill_validator() {
  local skill

  if (($# == 0)); then
    run_skill_validator_path "$SKILLS_ROOT"
    return $?
  fi

  for skill in "$@"; do
    run_skill_validator_path "$SKILLS_ROOT/$skill"
  done
}

run_skill_validator_path() {
  skill-validator check \
    --emit-annotations \
    --strict \
    --skip links \
    --allow-dirs agents,evals,examples,home \
    --allow-flat-layouts \
    "$1"
}

main() {
  validate_skill_args "$@" || return $?
  ensure_skill_validator || return $?
  ensure_eval_validator || return $?
  run_skill_validator "$@" || return $?
  run_eval_validator "$@" || return $?
}

main "$@"
