# 🧠 Sandhi Emotional Intelligence Dataset

> *A structured taxonomy mapping human emotions, cognitive patterns, and empathetic responses for advanced AI systems.*

![Taxonomy](https://img.shields.io/badge/Taxonomy-130_Categories-blue?style=for-the-badge&logo=hierarchy)
![Subcategories](https://img.shields.io/badge/Subcategories-711-brightgreen?style=for-the-badge)
![Format](https://img.shields.io/badge/Format-JSON-yellow?style=for-the-badge)
![RAG Ready](https://img.shields.io/badge/RAG-Ready-orange?style=for-the-badge)

## 📖 Overview

Welcome to the **Sandhi Emotional Intelligence Dataset**, the psychological core of the larger Sandhi project. 

This repository is a comprehensive, multi-dimensional emotional support and mental health dataset designed specifically to bridge the gap between factual AI and deeply human-centered emotional intelligence. It provides the structured knowledge required to power **Retrieval-Augmented Generation (RAG)**, **Fine-grained Emotion Tagging**, **User Personalization**, and **Long-term Episodic Memory Mapping**.

---

## 📂 Repository Structure

The dataset structure follows a strictly organized folder architecture designed for clean data pipelines:

```text
sandhi-emotional-intelligence-dataset/
├── README.md                           # This documentation
├── categories.csv                      # Flat CSV list of all 130 categories
│
├── taxonomy/                           # Schema and taxonomy files
│   ├── categories.json                 # Master list of category IDs & names
│   ├── emotions.json                   # Master subcategory taxonomy mapping
│   └── schemas/                        # Validation JSON Schemas
│
├── scripts/                            # Operational & automation scripts
│   ├── validate_taxonomy.py            # Integrity verification script
│   └── sync_emotions_json.py           # Syncs disk changes back to taxonomy
│
└── [130 Category Folders]/             # Root folders for each category (e.g., Exam Anxiety)
    └── [Subcategory Folders]/          # Subcategories (e.g., fear_of_failing)
        ├── inputs.json                 # User statements & contexts
        ├── responses.json              # Counseling support responses
        ├── evaluated.json              # Response safety & empathy scores
        ├── curated.json                # High-quality human-curated alignment pairs
        ├── metadata.json               # Clinical tags & subcategory info
        ├── variations.json             # Persona statements & lexicon
        ├── conversation_flows.json     # Counseling dialogue branch trees
        └── memory_patterns.json        # Cognitive distortion & episodic markers
```

---

## 🏷️ Emotional Taxonomy

The dataset captures **130 distinct main emotional categories** split into **711 high-fidelity subcategories** mapping to specific personal, academic, psychological, and social dimensions.

### Core Category Highlights

1. **`Exam Anxiety/`**
   * *Subcategories:* `fear_of_failing`, `parental_pressure`, `burnout`, `physical_panic_symptoms`, `time_pressure`...
2. **`Overthinking/`**
   * *Subcategories:* `rumination`, `decision_paralysis`, `catastrophizing`, `future_worry`...
3. **`Loneliness/`**
   * *Subcategories:* `social_anxiety`, `isolation`, `social_media_isolation`, `lack_of_belonging`...
4. **`Fear of Failure/`**
   * *Subcategories:* `perfectionism`, `imposter_syndrome`, `low_self_worth`, `shame_avoidance`...
5. **`Lack of Motivation/`**
   * *Subcategories:* `procrastination`, `executive_dysfunction`, `mental_fatigue`...
6. **`Comparison/`**
   * *Subcategories:* `social_media_envy`, `inferiority_complex`, `body_image_issues`...
7. **`Heartbreak/`**
   * *Subcategories:* `unrequited_love`, `loss_of_identity`, `denial_and_bargaining`...
8. **`Purpose Confusion/`**
   * *Subcategories:* `existential_dread`, `career_indecision`, `quarter_life_crisis`...
9. **`Self-Doubt/`**
   * *Subcategories:* `need_for_validation`, `fear_of_success`, `self_deprecating_talk`...
10. **`Discipline Problems/`**
    * *Subcategories:* `distraction`, `instant_gratification`, `poor_time_management`...

*(And 120 more categories spanning a vast spectrum of human emotion)*

---

## 🛠️ Operational Tooling

We have built a strict validation utility inside the `scripts/` directory to ensure perfect filesystem alignment:

```bash
python scripts/validate_taxonomy.py
```

This checks:
1. Integrity of the core JSON definitions.
2. Perfect alignment between `categories.json` and `emotions.json`.
3. Existence of all 130 root category folders and 711 subfolders on disk.

---

## 🚀 Use Cases in Production

### 1. High-Fidelity RAG Mappings
Files are heavily structured in JSON format. When querying an LLM, a RAG system can dynamically inject context from the relevant category folder (`conversation_flows.json`, `responses.json`), generating deeply empathetic and structurally sound responses.

### 2. Emotion Tagging & Memory Mapping
By classifying user inputs into the 711 subcategories, systems can construct a structured episodic vector database. Utilizing `memory_patterns.json`, agents can track cognitive distortions over time and establish persistent psychological context.

### 3. Contextual Personalization
If a user is persistently expressing `Comparison/social_media_envy`, an AI assistant can preemptively personalize its interactions, shifting tone and drawing from specific coping mechanisms relevant to that emotional state.
