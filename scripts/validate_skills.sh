#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_ROOT="${SKILLS_ROOT:-$ROOT/src}"
INSTALL_ROOT="${INSTALL_ROOT:-$HOME/.local}"
SKILL_VALIDATOR_VERSION="${SKILL_VALIDATOR_VERSION:-latest}"
SKILPEL_DOWNLOAD_BASE="${SKILPEL_DOWNLOAD_BASE:-https://github.com/pasunboneleve/skilpel/releases/latest/download}"
SKILPEL_CONFIG="${SKILPEL_CONFIG:-$ROOT/scripts/skilpel.yaml}"
SKILPEL_LOG_FORMAT="${SKILPEL_LOG_FORMAT:-auto}"
SKILPEL_OUTPUT="${SKILPEL_OUTPUT:-text}"
SKILPEL_WORKSPACE="${SKILPEL_WORKSPACE:-${TMPDIR:-/tmp}/skilpel-oiticica-style}"
SKILPEL="${SKILPEL:-$INSTALL_ROOT/bin/skilpel}"
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

ensure_skilpel() {
  local arch
  local asset
  local os
  local skilpel_dir
  local tmp

  if [[ -x "$SKILPEL" ]]; then
    return 0
  fi

  if ! command -v curl >/dev/null 2>&1; then
    printf 'error: skilpel is not installed and curl is unavailable to download it\n' >&2
    return 1
  fi

  if ! command -v shasum >/dev/null 2>&1; then
    printf 'error: skilpel is not installed and shasum is unavailable to verify it\n' >&2
    return 1
  fi

  case "$(uname -s)" in
    Linux)
      os=linux
      ;;
    Darwin)
      os=darwin
      ;;
    *)
      printf 'error: unsupported skilpel release platform: %s\n' "$(uname -s)" >&2
      return 1
      ;;
  esac

  case "$(uname -m)" in
    x86_64 | amd64)
      arch=amd64
      ;;
    arm64 | aarch64)
      arch=arm64
      ;;
    *)
      printf 'error: unsupported skilpel release architecture: %s\n' "$(uname -m)" >&2
      return 1
      ;;
  esac

  asset="skilpel-$os-$arch"
  skilpel_dir="$(dirname "$SKILPEL")"
  tmp="$(mktemp -d "${TMPDIR:-/tmp}/skilpel-download.XXXXXX")" || return $?
  local status=0

  (
    set -euo pipefail
    curl -fsSL "$SKILPEL_DOWNLOAD_BASE/$asset" -o "$tmp/$asset"
    curl -fsSL "$SKILPEL_DOWNLOAD_BASE/$asset.sha256" -o "$tmp/$asset.sha256"
    (cd "$tmp" && shasum -a 256 -c "$asset.sha256")

    mkdir -p "$skilpel_dir"
    install -m 0755 "$tmp/$asset" "$SKILPEL"
  ) || status=$?
  rm -rf "$tmp"
  return "$status"
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

run_skilpel() {
  local run_workspace
  local skill
  local skill_args=()

  for skill in "$@"; do
    skill_args+=(--skill "$skill")
  done

  run_workspace="$(mktemp -d "${SKILPEL_WORKSPACE%/}.XXXXXX")" || return $?

  "$SKILPEL" run \
    --config "$SKILPEL_CONFIG" \
    --root "$SKILLS_ROOT" \
    --workspace "$run_workspace" \
    --log-format "$SKILPEL_LOG_FORMAT" \
    --output "$SKILPEL_OUTPUT" \
    "${skill_args[@]}"
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
  ensure_skilpel || return $?
  run_skill_validator "$@" || return $?
  run_skilpel "$@" || return $?
}

main "$@"
