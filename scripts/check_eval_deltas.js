#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

const workspace = process.argv[2];
const minDelta = Number(process.argv[3]);
const minPass = Number(process.argv[4]);

if (!workspace) {
  console.error("error: workspace path is required");
  process.exit(1);
}

if (!Number.isFinite(minDelta)) {
  console.error(`error: AGENT_SKILLS_EVAL_MIN_DELTA must be a number, got ${process.argv[3]}`);
  process.exit(1);
}

if (!Number.isFinite(minPass)) {
  console.error(`error: AGENT_SKILLS_EVAL_MIN_PASS must be a number, got ${process.argv[4]}`);
  process.exit(1);
}

function findBenchmarks(dir) {
  const found = [];

  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      found.push(...findBenchmarks(fullPath));
    } else if (entry.isFile() && entry.name === "benchmark.json") {
      found.push(fullPath);
    }
  }

  return found;
}

function pct(value) {
  return `${(value * 100).toFixed(1)}pp`;
}

const benchmarks = findBenchmarks(workspace);
let failed = false;

if (benchmarks.length === 0) {
  console.error(`error: no agent-skills-eval benchmark.json files found under ${workspace}`);
  process.exit(1);
}

for (const benchmarkPath of benchmarks) {
  const benchmark = JSON.parse(fs.readFileSync(benchmarkPath, "utf8"));
  const delta = benchmark?.run_summary?.delta?.pass_rate;
  const withSkill = benchmark?.run_summary?.with_skill?.pass_rate?.mean;
  const withoutSkill = benchmark?.run_summary?.without_skill?.pass_rate?.mean;

  if (![delta, withSkill, withoutSkill].every(Number.isFinite)) {
    console.error(`error: benchmark lacks baseline pass-rate summary: ${benchmarkPath}`);
    failed = true;
    continue;
  }

  if (delta < minDelta) {
    console.error(
      `error: skill eval delta too small for ${benchmarkPath}: ` +
        `${pct(delta)} < ${pct(minDelta)} ` +
        `(with_skill ${pct(withSkill)}, without_skill ${pct(withoutSkill)})`
    );
    failed = true;
  }

  if (withSkill < minPass) {
    console.error(
      `error: skill eval pass rate too small for ${benchmarkPath}: ` +
        `${pct(withSkill)} < ${pct(minPass)} ` +
        `(delta ${pct(delta)}, without_skill ${pct(withoutSkill)})`
    );
    failed = true;
  }
}

if (failed) {
  process.exit(1);
}
