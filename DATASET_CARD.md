# Sandhi Memory Mapping Dataset Card

## Dataset Overview
The Sandhi Memory Mapping Dataset is organized into two primary sections:
- **Sandhi Emotional Intelligence Dataset**: 130 categories and 713 subcategories of emotional states with structured JSON files for inputs, responses, evaluations, memory patterns, and conversation flows.
- **Sandhi Spiritual Intelligence Dataset**: 5 collections of structured wisdom entries (Hitopadesa, Mahabharata, Pursuit of God, Swami Sivananda, Yoga Sutras).

Repository-wide statistics are available in [statistics.md](statistics.md) and [statistics.json](statistics.json).

## Motivation
The dataset is designed to bridge factual AI systems with human-centered emotional intelligence and spiritual grounding. The repository structure and JSON schemas aim to support memory-aware assistants, reflective RAG workflows, and empathetic response generation.

## Intended Use
- Retrieval-Augmented Generation (RAG) for emotional support and reflective guidance.
- Long-term memory mapping using `memory_patterns.json` and structured subcategory metadata.
- Dataset exploration, taxonomy research, and educational tooling built on the emotional/spiritual hierarchies.

## Out-of-Scope Use
- Clinical diagnosis, therapy, or crisis intervention without qualified human oversight.
- Automated decision-making affecting health, legal, or financial outcomes.
- Any use that violates the original source terms or privacy expectations of collected content.

## Dataset Structure
- **Root**: `sandhi-emotional-intelligence-dataset/` and `sandhi-spritual-intelligence-dataset/`.
- **Emotional Dataset**: Each subcategory folder contains a consistent set of JSON files (`inputs.json`, `responses.json`, `evaluated.json`, `curated.json`, `metadata.json`, `variations.json`, `conversation_flows.json`, `memory_patterns.json`).
- **Spiritual Dataset**: Each entry JSON file contains structured fields such as `text`, `modern_interpretation`, `emotion_tags`, and `actionable_advice`, with `_index.json` providing the master index.

## Data Sources
- The emotional dataset includes references to public online discussions in `sandhi_dataset_pipeline/raw_data/raw_posts.json` (fields include subreddit, title, body, and score).
- The spiritual dataset is organized around named source texts (e.g., Hitopadesa, Mahabharata, Yoga Sutras, Swami Sivananda, Pursuit of God) as indicated by folder names and per-entry metadata.
- The repository README also notes the use of public discussions, Q&A platforms, and synthetic examples; these should be verified before production use.

## Collection Methodology
- The `sandhi_dataset_pipeline/scripts` directory includes scripts such as `scrape_reddit.py`, `process_emotions.py`, `generate_responses.py`, and `evaluate_responses.py`.
- Processed outputs in `processed_data/` and `outputs/` demonstrate the transformation from raw posts to structured inputs, responses, and evaluations.

## Processing Pipeline
1. **Raw ingestion**: `raw_data/raw_posts.json` collects source posts.
2. **Processing**: `processed_data/inputs.json` maps raw posts into structured emotional inputs.
3. **Response generation**: `outputs/responses.json` stores generated responses.
4. **Evaluation**: `outputs/evaluated.json` captures scoring and approval metadata for responses.

## Known Limitations
- Token counts are not computed in the repository because a tokenizer library is not bundled (see statistics output).
- No formal JSON Schema files are provided; schemas are inferred from the existing JSON structures.
- Source licensing metadata for original materials is not recorded per entry.

## Biases
- Emotional data includes public forum posts and curated synthetic samples, which may reflect demographic, cultural, and platform-specific biases.
- Spiritual content focuses on specific traditions and authors, which may not represent all philosophical perspectives.

## Safety Considerations
- Content includes mental health topics; systems built on this dataset should provide safe, non-clinical guidance and route critical cases to qualified professionals.
- Avoid using the dataset to produce prescriptive medical or legal advice.

## Ethical Considerations
- Respect privacy expectations for public posts and ensure compliance with original platform terms.
- Use transparent disclosure when deploying models trained or retrieved from this dataset.

## Licensing Notes
- The repository README references the MIT License, but a root `LICENSE` file is not present in this repository snapshot. Verify licensing before redistribution.
- **Source licensing may vary depending on original source material and should be independently reviewed before production use.**

## Citation Information
```bibtex
@dataset{sandhi_dataset_2026,
  author       = {Muskan Kumar and Contributors},
  title        = {Sandhi Memory Mapping Dataset: A Structured Emotional and Spiritual AI Knowledge Base},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/muskan-kumar-ece/sandhi-memory-mapping-dataset}}
}
```

## Version Information
- No formal version tags are present in the repository.
- Documentation generated on 2026-06-04.
