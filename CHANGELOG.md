# Changelog

All notable changes to this repository are documented in this file.

This project uses SemVer. Version tags use the `vMAJOR.MINOR.PATCH` format.

## [Unreleased]

### Changed

- Make single-passage audits explicit in both aggregate style skills, and make
  `oiticica-style-qualities` invoke its six component skills by `$` handle.

## [0.4.0] - 2026-08-13

### Added

- Added `oiticica-style-defects`, a fixed six-defect audit for diagnosing and
  comparing drafts with concrete evidence and narrow follow-up handles.

### Changed

- Validate every skill with GPT-5.6 Luna through one shared model
  configuration.

### Fixed

- Require the general style router to repair causal order without merely
  repunctuating the sequence or changing an event’s actor, action, or object.
- Require generic-description revisions to replace evaluative praise with
  observable detail rather than new praise synonyms.
- Judge the router’s ambiguity diagnosis by whether it names both possible
  reviewers, independent of which response section contains the evidence.
- Accept concrete, skill-relevant fault evidence across every generated repair
  eval, and use an unambiguous Federalist No. 10 comma model.
- Replace the accumulation eval’s hypothetical passage with the sourced full
  opening sentence of *Paul Clifford* and preserve its quotation boundary.

## [0.3.0] - 2026-06-26

### Added

- Linked skills into `~/.agents/skills` for Pi-compatible agent installs.

### Documentation

- Updated the README to position the repository for Codex, Claude Code, and Pi, with links to each agent's website.

## [0.2.1] - 2026-05-25

### Changed

- Moved generated skill source notes from `agents/notes.md` to `references/notes.md`.
- Explicitly request `skilpel` text summaries in skill validation while keeping
  the latest-release executable download.

### Fixed

- Replaced positive skill eval source-model paraphrases with exact public-domain quotations and recorded exact source references in `references/notes.md`.

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
