# Evaluation-Gated RAG over Kubernetes v1.36 Documentation

A retrieval-augmented generation system over the Kubernetes v1.36
documentation, built with a CI-gated evaluation harness: golden-set retrieval
metrics (recall@10, nDCG@10), a human-calibrated LLM faithfulness judge, and a
corpus provenance check — delivered through a free public demo.

The project is built incrementally from a naive baseline, with each optimisation
introduced as a single-variable change and measured against the previous step.
The ablation table is the primary deliverable; the code exists to produce it.

## Status

Session 1 complete: scaffold, guardrails, frozen corpus, corpus manifest,
first commit. Pipeline stages land in subsequent sessions.

## Corpus provenance

- Source: `kubernetes/website`, branch `release-1.36`
- Commit: `1de955ebabe7e17da1ebb4f582635491227f4157`
- Markdown files hashed: 1672
- Manifest: `corpus_manifest.json` (SHA256 per file)

The corpus is pinned to a single release commit and treated as immutable. The
SHA256 manifest verifies that the checked-out documentation matches the commit
the evaluation results were measured against — it is a **provenance check**,
not a drift detector. See "Future Work" for what a real drift detector would
require.

## Future Work

**Corpus drift detection.** This project pins the Kubernetes documentation to
the v1.36 release commit and treats the pinned corpus as immutable. The SHA256
manifest in `corpus_manifest.json` verifies corpus *provenance* — it confirms
that the checked-out docs match the commit the results were measured against.

True drift detection would require:

- Per-chunk content hashing to detect sub-file changes
- Embedding-level drift scoring (cosine distance between old and new chunk
  embeddings) to distinguish cosmetic edits from semantic changes
- A scheduled canary that re-runs the held-out evaluation against the latest
  upstream docs and reports whether the system's quality has degraded

This is out of scope for a single-release project, where the corpus is frozen
by design. It would be the first extension in a multi-version deployment.