# Documentation Audit

## Missing Documentation
- `LICENSE` file is not present in the repository root (referenced in README).
- `CONTRIBUTING.md` is referenced in README but not present.
- No README is present inside `sandhi_dataset_pipeline/` to explain the pipeline inputs/outputs and execution.
- No formal release/version notes are included.

## Missing Metadata
- No per-entry licensing metadata for spiritual sources.
- No source URL or attribution fields in `raw_posts.json` or pipeline artifacts beyond subreddit/title/body.
- Emotional dataset entries do not include language, region, or collection timestamp metadata.

## Potential Licensing Concerns
- The README references the MIT License, but the corresponding `LICENSE` file is missing.
- Source licensing for forum posts and spiritual texts is not documented per entry and may vary by origin.

## Schema Inconsistencies
- No missing subcategory JSON files were detected; each subcategory includes the expected file set.
- Pipeline outputs (`processed_data/inputs.json`, `outputs/responses.json`, `outputs/evaluated.json`) use a reduced field set compared to the full subcategory schema, which should be documented for downstream consumers.

## Empty Folders
- No empty directories detected in the repository.

## Broken References
- Root README links to `CONTRIBUTING.md` and `LICENSE`, which are not present.
- `sandhi-emotional-intelligence-dataset/README.md` references a `scripts/` directory that does not exist in that dataset folder.
- `sandhi-emotional-intelligence-dataset/FOLDER_STRUCTURE.md` references `c:/workflow/sandhidataset`, which does not match the current repository pathing.

## Duplicate Structures
- Each emotional subcategory repeats the same standardized JSON file set (`inputs.json`, `responses.json`, `evaluated.json`, `curated.json`, `metadata.json`, `variations.json`, `conversation_flows.json`, `memory_patterns.json`). This duplication is expected but increases storage size and should be considered in downstream tooling.
