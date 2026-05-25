# Changelog

All notable changes to this repository are documented in this file.

This project uses SemVer. Version tags use the `vMAJOR.MINOR.PATCH` format.

## [Unreleased]

## [0.2.1] - 2026-05-25

### Changed

- Moved generated skill source notes from `agents/notes.md` to `references/notes.md`.
- Explicitly request `skilpel` text summaries in skill validation while keeping
  the latest-release executable download.

### Fixed

- Replaced positive skill eval source-model paraphrases with exact public-domain quotations and recorded exact source references in agent notes.

### Documentation

- Added README validation and release badges.
- Documented the `skilpel` validation output split and `SKILPEL_OUTPUT=json`
  override.

## [0.2.0] - 2026-05-24

### Changed

- Switched repository task-tracking workflow instructions to Kata.
- Changed generated skill eval files from JSON to YAML.
- Replaced `agent-skills-eval` validation with latest-release `skilpel` validation.
- Preserved model-backed validation defaults in `scripts/skilpel.yaml`.
- Tightened `oiticica-style` preservation and ambiguity routing evals for released `skilpel` validation.

### Fixed

- Clean up temporary `skilpel` download directories and preserve download or checksum failures during validation.
- Force pretty `skilpel` progress logs in GitHub Actions validation.

## [0.1.1] - 2026-05-21

### Changed

- Linked the contribution guide mentions of `skill-validator` to its upstream repository.
- Linked documentation mentions of Codex to the Codex CLI documentation.

## [0.1.0] - 2026-05-21

### Added

- Added the standalone Oiticica style skill catalogue with generated principle skills.
- Added `oiticica-style`, a router skill that selects relevant principle skills by identifying genre, eliminating defects, and applying qualities only where needed.
- Added validation, linking, and CI scripts for local Codex and Claude skill use.
- Added contribution documentation for validation tooling and model-backed eval behavior.
