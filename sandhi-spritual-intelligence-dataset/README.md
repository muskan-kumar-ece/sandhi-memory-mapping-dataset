# 🧘 Sandhi Spiritual Intelligence Dataset

> *A structured compendium of ancient wisdom, philosophy, and contemplative knowledge designed to give AI a sense of meaning and ethical depth.*

![Wisdom Sources](https://img.shields.io/badge/Sources-Diverse-blue?style=for-the-badge&logo=book)
![Focus](https://img.shields.io/badge/Focus-Philosophy_&_Reflection-brightgreen?style=for-the-badge)
![Format](https://img.shields.io/badge/Format-JSON-yellow?style=for-the-badge)
![AI Ready](https://img.shields.io/badge/AI-Ready-orange?style=for-the-badge)

## 📖 Overview

Welcome to the **Sandhi Spiritual Intelligence Dataset**, a curated repository designed to ground AI models in meaning-seeking, existential reflection, and life wisdom.

While the Emotional Dataset focuses on psychological states, the Spiritual Dataset provides the structural knowledge required for agents to engage in high-level contemplation. By mapping texts from global wisdom traditions into clean, structured JSON schemas, we enable AI to offer perspective, resilience, and philosophical grounding.

---

## 📂 Repository Structure

The dataset categorizes profound philosophical texts into distinct collections:

```text
sandhi-spritual-intelligence-dataset/
├── README.md                           # This documentation
├── _index.json                         # Master index mapping all entries, tags, and styles
│
├── hitopadesa/                         # The Book of Good Counsels
├── mahabharata/                        # Epic wisdom, leadership, and duty
├── pursuit-of-god/                     # Deep devotional and existential reflections
├── swami-sivananda/                    # Yogic practices, discipline, and inner peace
└── yoga-sutras/                        # Mind mastery, detachment, and consciousness
```

---

## 🏷️ Knowledge Domains & Taxonomy

Each text is heavily processed and categorized based on multiple dimensions of human experience, mapped precisely in `_index.json`.

### Wisdom Styles
- **Philosophical:** Existential inquiry and meaning.
- **Stoic:** Resilience, acceptance, and endurance.
- **Strategic:** Discernment, leadership, and practical action.
- **Devotional:** Surrender, faith, and inner connection.
- **Yogic/Vedantic:** Mind mastery, discipline, and non-dual understanding.

### Guidance Types
The dataset labels every piece of knowledge with actionable guidance types, such as:
- Emotional Regulation
- Self Inquiry & Mindfulness
- Courage & Resilience
- Karma Yoga (Action without attachment)
- Detachment & Simplification

### Emotion & Problem Tags
Wisdom entries are directly tied to human struggles. The metadata contains hundreds of tags mapping ancient texts to modern problems:
- **Emotion Tags:** *Existential Dread, Imposter Syndrome, Restlessness, Arrogance, Compassion, Inner Peace, Despair, Hope.*
- **Problem Tags:** *Career Stagnation, Burnout, Decision Fatigue, Imposter Syndrome, Materialism, Toxic Relationships, Spiritual Void.*

---

## 🧩 Example Mapping

The dataset allows an AI to understand that a user experiencing `Burnout` or `Existential Dread` might benefit from specific teachings on *Detachment* or *Resilience* found in the **Bhagavad Gita (Mahabharata)** or the **Yoga Sutras**.

Every entry includes attributes linking it to these structured tags, making it incredibly powerful for search and retrieval.

### Data Collection & Generation
To collect and generate this structured wisdom dynamically, we utilize the Gemini-powered pipeline located in the companion `sandhi-emotional-intelligence-dataset/sandhi_dataset_pipeline` directory. Ensure you set up your `.env` file with your `GEMINI_API_KEY` before running the pipeline.

---

## 🚀 Use Cases in Production

### 1. Journaling and Reflection AI
Use the dataset to power apps that help users explore their values, confront existential challenges, or reflect on their daily lives using timeless wisdom.

### 2. Meaning-Aware RAG Pipelines
Augment a standard RAG chatbot with spiritual intelligence. When a user asks a deep, philosophical question about purpose, the agent can retrieve structured, verified wisdom rather than generating generic advice.

### 3. Ethical and Stoic Coaching
Train or prompt AI models using the "Stoic" or "Strategic" wisdom styles to act as a resilient coach for users facing extreme adversity or complex leadership challenges.

### 4. Holistic Mental Wellbeing
Combine this dataset with the **Emotional Intelligence Dataset** to provide a dual-layered support system: psychological coping mechanisms (Emotional) paired with deeper meaning-making and perspective-shifting (Spiritual).
