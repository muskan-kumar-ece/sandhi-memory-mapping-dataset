import json
import os
import re
from dotenv import load_dotenv

# Try importing google.generativeai
try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
is_placeholder = not api_key or "your_gemini_api_key" in api_key

# ----------------- Fallback Procedural Classifier -----------------
# We define keyword rules mapping raw texts to our Sandhi categories & subcategories
RULE_MAPPINGS = [
    {
        "keywords": ["exam", "fail", "marks", "test", "grade", "results", "syllabus", "study", "studying"],
        "category": "Exam Anxiety",
        "subcategory": "fear_of_failing",
        "emotion": "fear",
        "thought_pattern": "catastrophizing",
        "lexicon": ["exam", "study", "fail", "score"]
    },
    {
        "keywords": ["parent", "father", "mother", "papa", "mom", "dad", "family", "relative"],
        "category": "Parental Pressure",
        "subcategory": "parental_expectations",
        "emotion": "shame",
        "thought_pattern": "comparison",
        "lexicon": ["parents", "expectations", "compare"]
    },
    {
        "keywords": ["lonely", "alone", "friend", "mess", "hostel", "social", "isolate", "invisible"],
        "category": "Loneliness",
        "subcategory": "no_friends",
        "emotion": "sadness",
        "thought_pattern": "isolation",
        "lexicon": ["alone", "loneliness", "no_friends"]
    },
    {
        "keywords": ["burnout", "tired", "exhaust", "maggi", "coffee", "sleep", "drain"],
        "category": "Burnout",
        "subcategory": "exhaustion",
        "emotion": "numbness",
        "thought_pattern": "overwhelming",
        "lexicon": ["exhausted", "burnout", "tired"]
    },
    {
        "keywords": ["overthink", "worry", "catastrophize", "what if", "mind", "brain", "rumination"],
        "category": "Overthinking",
        "subcategory": "rumination",
        "emotion": "anxiety",
        "thought_pattern": "rumination",
        "lexicon": ["overthinking", "what ifs", "worry"]
    }
]

def procedural_structure(title, body):
    combined = (title + " " + body).lower()
    
    # Defaults
    category = "Self-Doubt"
    subcategory = "imposter_syndrome"
    emotion = "fear"
    thought_pattern = "catastrophizing"
    intensity = 7
    
    # Try rule matching
    for rule in RULE_MAPPINGS:
        if any(kw in combined for kw in rule["keywords"]):
            category = rule["category"]
            subcategory = rule["subcategory"]
            emotion = rule["emotion"]
            thought_pattern = rule["thought_pattern"]
            intensity = 8 if any(k in combined for k in ["kill", "die", "extended", "loan", "severe", "worst"]) else 6
            break
            
    # Clean user input statement to keep it punchy and realistic
    user_input = body[:120].strip() + "..." if len(body) > 120 else body.strip()
    if not user_input or len(user_input) < 10:
        user_input = title.strip()
        
    return {
        "emotion": emotion,
        "emotion_intensity": intensity,
        "thought_pattern": thought_pattern,
        "user_input": user_input,
        "category": category,
        "subcategory": subcategory
    }

# ----------------- Execution Main -----------------

raw_posts_path = r"c:\workflow\sandhi-memory-mapping-dataset\sandhi-emotional-intelligence-dataset\sandhi_dataset_pipeline\raw_data\raw_posts.json"
processed_data_dir = r"c:\workflow\sandhi-memory-mapping-dataset\sandhi-emotional-intelligence-dataset\sandhi_dataset_pipeline\processed_data"

print("Beginning AI Emotional Structuring Engine...")

with open(raw_posts_path, "r", encoding="utf-8") as f:
    posts = json.load(f)

processed_data = []

# Target the first 20 posts as requested
target_posts = posts[:20]

if HAS_GENAI and not is_placeholder:
    print("Valid Gemini API Key found. Using Google Generative AI (gemini-2.5-flash)...")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    for i, post in enumerate(target_posts):
        raw_text = f"Title: {post['title']}\nBody: {post['body']}"
        
        prompt = f"""
        Extract emotional information from this Reddit post.

        Return ONLY a raw valid JSON block. DO NOT write markdown formatting like ```json or ```. Just raw JSON.

        Format:
        {{
          "emotion": "primary emotion tag (e.g. fear, anxiety, shame, sadness)",
          "emotion_intensity": integer between 1-10,
          "thought_pattern": "cognitive style (e.g. catastrophizing, comparison, overthinking)",
          "user_input": "summarized punchy single-sentence emotional statement from the text",
          "category": "matching main emotional category (e.g. Exam Anxiety, Loneliness, Overthinking, Parental Pressure)",
          "subcategory": "matching taxonomy subcategory (e.g. fear_of_failing, no_friends, rumination, parental_expectations)"
        }}

        Text:
        {raw_text}
        """
        
        try:
            response = model.generate_content(prompt)
            cleaned = response.text.replace("```json", "").replace("```", "").strip()
            # Strict regex clean to strip extra text if LLM includes it
            json_match = re.search(r'\{.*\}', cleaned, re.DOTALL)
            if json_match:
                cleaned = json_match.group(0)
            
            processed_data.append(json.loads(cleaned))
            print(f"[{i+1}/20] Successfully structured post via Gemini.")
        except Exception as e:
            print(f"[{i+1}/20] AI API error: {e}. Falling back to rule-based parser.")
            processed_data.append(procedural_structure(post["title"], post["body"]))
else:
    print("No valid Gemini API key found (placeholder or missing). Using Rule-Based NLP Classifier Fallback...")
    for i, post in enumerate(target_posts):
        processed_data.append(procedural_structure(post["title"], post["body"]))
        print(f"[{i+1}/20] Structured post via rule-based classifier.")

os.makedirs(processed_data_dir, exist_ok=True)
output_path = os.path.join(processed_data_dir, "inputs.json")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(processed_data, f, indent=2, ensure_ascii=False)

print(f"\nProcessing Complete! Saved {len(processed_data)} structured inputs to {output_path}")
