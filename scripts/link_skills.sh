#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
repo_root="$(cd -- "${script_dir}/.." && pwd -P)"
skills_root="${SKILLS_ROOT:-${repo_root}/src}"
codex_home="${CODEX_HOME:-${HOME}/.codex}"
dest_root="${CODEX_SKILLS_DIR:-${codex_home}/skills}"
claude_home="${CLAUDE_HOME:-${HOME}/.claude}"
claude_skills_dir="${CLAUDE_SKILLS_DIR:-${claude_home}/skills}"

linked=0
skipped=0
failed=0
unlinked=0

unlink_dead_links() {
  local dir="$1"
  local link

  [[ -d "${dir}" ]] || return 0

  while IFS= read -r -d '' link; do
    unlink -- "${link}"
    printf 'unlink: %s\n' "${link}"
    unlinked=$((unlinked + 1))
  done < <(find "${dir}" -maxdepth 1 -type l ! -exec test -e {} \; -print0 | sort -z)
}

link_skill_dir() {
  local skill_dir="$1"
  local dest="$2"

  if [[ -e "${dest}" && ! -L "${dest}" ]]; then
    printf 'error: %s exists and is not a symlink\n' "${dest}" >&2
    failed=$((failed + 1))
  elif [[ -L "${dest}" && "$(readlink -- "${dest}")" == "${skill_dir}" ]]; then
    printf 'skip: %s -> %s\n' "${dest}" "${skill_dir}"
    skipped=$((skipped + 1))
  else
    ln -sfn -- "${skill_dir}" "${dest}"
    printf 'link: %s -> %s\n' "${dest}" "${skill_dir}"
    linked=$((linked + 1))
  fi
}

unlink_dead_links "${dest_root}"
unlink_dead_links "${claude_skills_dir}"

mkdir -p -- "${dest_root}" "${claude_skills_dir}"

while IFS= read -r -d '' skill_file; do
  skill_dir="$(dirname -- "${skill_file}")"
  skill_name="$(basename -- "${skill_dir}")"

  link_skill_dir "${skill_dir}" "${dest_root}/${skill_name}"
  link_skill_dir "${skill_dir}" "${claude_skills_dir}/${skill_name}"
done < <(find "${skills_root}" -type f -name SKILL.md -print0 | sort -z)

printf 'done: %d linked, %d skipped, %d unlinked, %d failed\n' "${linked}" "${skipped}" "${unlinked}" "${failed}"

if ((failed > 0)); then
  exit 1
fi
