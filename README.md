<div align="center">
  
# 🌊 Sandhi Memory Mapping Dataset

**Bridging the gap between factual AI and human-centered emotional intelligence.**

[![Dataset](https://img.shields.io/badge/Dataset-Sandhi-0052CC?style=for-the-badge&logo=data)](#)
[![Open Source](https://img.shields.io/badge/Open_Source-MIT-2EA44F?style=for-the-badge)](#)
[![RAG Ready](https://img.shields.io/badge/RAG-Ready-FF7139?style=for-the-badge)](#)
[![Format](https://img.shields.io/badge/Format-JSON-F7DF1E?style=for-the-badge)](#)
[![AI Ready](https://img.shields.io/badge/AI-Ready-6B46C1?style=for-the-badge)](#)

*A massive, structured knowledge base designed to give agents memory, empathy, and philosophical grounding.*

---

</div>

## 📖 Overview

The **Sandhi Memory Mapping Dataset** is a comprehensive, multi-dimensional repository (664.00 MB on disk; see [statistics.md](statistics.md)) built to empower artificial intelligence with deep emotional intelligence and spiritual understanding. 

While modern Large Language Models (LLMs) excel at reasoning and factual recall, they fundamentally lack the structural grounding required to engage with the complex dimensions of human experience—empathy, memory, meaning-seeking, and vulnerability. 

Sandhi solves this by providing the exact cognitive schemas required to build **memory-aware assistants**, **personalized RAG pipelines**, and **wellbeing applications** that truly understand the user over time.

---

## 🌟 Key Capabilities

- **Deep Emotional Taxonomy:** Curated mappings for hundreds of complex emotional states, moving far beyond basic sentiment analysis (e.g., from *Abandonment Issues* to *Toxic Positivity Exhaustion*).
- **Philosophical & Spiritual Grounding:** Includes a dedicated spiritual dataset designed to help models navigate life wisdom, existential reflection, and self-awareness.
- **Long-Term Episodic Memory:** Structured JSON schemas capture cognitive distortions, coping mechanisms, and episodic triggers, enabling agents to form persistent user memories.
- **Plug-and-Play RAG Integration:** Designed from the ground up for modern AI pipelines. The data is pre-chunked into clean JSON, ready for immediate embedding and retrieval.

---

## 📚 Documentation

- **Dataset Card:** [DATASET_CARD.md](DATASET_CARD.md)
- **Schema Documentation:** [SCHEMA.md](SCHEMA.md)
- **Dataset Statistics:** [statistics.md](statistics.md) / [statistics.json](statistics.json)

## 🏗 Dataset Architecture

The repository is logically divided into two major domains:

```text
sandhi-memory-mapping-dataset/
├── 🧠 sandhi-emotional-intelligence-dataset/  # 130 Categories of Emotional States
│   ├── Abandonment Issues/                    # Example Category
│   │   ├── fear_of_rejection/                 # Subcategory
│   │   │   ├── responses.json                 # Empathetic AI responses
│   │   │   ├── memory_patterns.json           # Cognitive tracking
│   │   │   └── ...
│   └── ...
└── 🧘 sandhi-spritual-intelligence-dataset/   # Philosophy, Contemplation & Wisdom
    ├── hitopadesa/                            # Strategy & Discernment
    ├── mahabharata/                           # Resilience & Duty
    ├── pursuit-of-god/                        # Devotion & Existential Reflection
    ├── swami-sivananda/                       # Discipline & Emotional Regulation
    └── yoga-sutras/                           # Mind Mastery & Detachment
```

---

## 📊 Dataset Statistics

| Metric | Count / Size | Description |
| :--- | :--- | :--- |
| **Total Size** | `664.00 MB` | Uncompressed files on disk. |
| **Approx. Tokens** | `Not computed` | Tokenizer not bundled; see statistics. |
| **Domains** | `2` | Emotional Intelligence & Spiritual Intelligence. |
| **Categories** | `130` | Top-level emotional categories. |
| **Subcategories** | `713` | Emotional subcategories. |
| **JSON Files** | `5,779` | Structured files on disk. |
| **Total Records** | `1,144,125` | Top-level JSON items across files. |

---

## ✅ Dataset Validation and Quality Assurance

- `scripts/dataset_statistics.py` computes file counts, sizes, and record totals; outputs are in `statistics.json` and `statistics.md`.
- The `sandhi-emotional-intelligence-dataset/taxonomy/` directory provides authoritative category and subcategory lists for manual validation.
- Each emotional subcategory folder contains a consistent set of JSON files (inputs, responses, evaluations, curated pairs, metadata, variations, flows, memory patterns).
- No automated test suite or linting configuration is included in the repository; validation is currently manual and script-assisted.

---

## 🔬 Data Collection Methodology

The dataset was developed through a combination of:

- Publicly available discussions and community conversations
- Open question-and-answer platforms
- Public forum discussions
- Public comments and feedback datasets
- Educational and self-improvement content
- Human-curated emotional and spiritual knowledge structures
- Synthetic examples generated for coverage and balance

All collected information was transformed into structured knowledge representations and organized into a standardized taxonomy designed for AI applications, Retrieval-Augmented Generation (RAG), personalization systems, and emotional intelligence research.

### Automated Data Collection Pipeline
This repository includes a `sandhi_dataset_pipeline` directory within the emotional intelligence dataset. It contains an automated, Gemini API-powered pipeline to scrape, structure, and evaluate new data directly into the dataset format. To use it, simply configure a `.env` file with `GEMINI_API_KEY` and run `run_pipeline.py`.

---

## 💻 Quick Start & Usage

Sandhi is built for immediate integration into Python-based AI workflows.

```python
import json
import os

# Example: Loading a user's memory pattern for a personalized agent
dataset_path = "sandhi-emotional-intelligence-dataset"
category_path = os.path.join(dataset_path, "Abandonment Issues", "fear_of_rejection")

with open(os.path.join(category_path, "memory_patterns.json"), "r") as f:
    memory_schema = json.load(f)

print(f"Detected Cognitive Distortion: {memory_schema['cognitive_distortion']}")
print(f"Recurrent Themes: {', '.join(memory_schema['recurrent_themes'])}")

# Inject this context directly into your LLM's system prompt!
```

**`memory_patterns.json` Output:**
```json
{
  "cognitive_distortion": "overgeneralization",
  "recurrent_themes": ["fear of rejection", "academic_standing", "social_evaluation"],
  "coping_history": "avoidant_behavior",
  "episodic_markers": {
    "frequency": "recurrent_under_high_stress",
    "trigger_sensitivity": "high_during_exams"
  }
}
```

---

## 🚀 Production Use Cases

> *"True artificial intelligence is not just about understanding the world—it is about understanding the human experiencing it."*

| Use Case | Implementation Strategy |
| :--- | :--- |
| **🔍 Contextual RAG** | Inject specific `responses.json` and `conversation_flows.json` into the LLM context window based on the user's detected emotional state. |
| **👤 Personalized Agents** | Utilize `memory_patterns.json` to track episodic markers across sessions, giving the agent a long-term memory of the user's psychological triggers. |
| **🌿 Mental Wellbeing Apps** | Power safe, supportive, and context-aware journaling companions backed by curated therapeutic frameworks. |
| **🧠 Meaning-Aware Systems** | Route existential or philosophical queries to the Spiritual Dataset to provide deep, reflective wisdom rather than generic chatbot answers. |

---

## 🗺️ Roadmap

- [ ] **Expanded Categories:** Adding granular coverage for workplace burnout, neurodivergent experiences, and grief.
- [ ] **Multilingual Support:** Translating core datasets into Spanish, French, and Mandarin.
- [ ] **Vector Search Optimization:** Providing pre-computed metadata formats specifically for Pinecone and Milvus.
- [ ] **Embeddings Release:** Releasing open-source embeddings natively tuned for the Sandhi schema.
- [ ] **Agentic Framework Integration:** Native loaders for LangChain and LlamaIndex.

---

## 🤝 Contributing

We welcome contributions from AI researchers, developers, psychologists, and philosophers! 

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) to learn how you can help expand the dataset, improve JSON schemas, or suggest new categories for human experience.

---

## 📜 License

This dataset is released under the **[MIT License](LICENSE)**.

---

## 📝 Citation

If you use the Sandhi Dataset in your research, academic paper, or production application, please cite us:

```bibtex
@dataset{sandhi_dataset_2026,
  author       = {Muskan Kumar and Contributors},
  title        = {Sandhi Memory Mapping Dataset: A Structured Emotional and Spiritual AI Knowledge Base},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/muskan-kumar-ece/sandhi-memory-mapping-dataset}}
}
```
