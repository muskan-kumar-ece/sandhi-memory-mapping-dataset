import json
import os
from dotenv import load_dotenv

try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
is_placeholder = not api_key or "your_gemini_api_key" in api_key

# ----------------- Fallback Procedural Response Database -----------------
RESPONSE_DATABASE = {
    "fear_of_failing": {
        "response_style": "grounding",
        "sandhi_response": "Right now your mind is treating one exam like your entire future. Fear becomes overwhelming when everything feels attached to one outcome.",
        "wisdom_theme": "detachment",
        "tone": "calm",
        "length": "medium"
    },
    "parental_expectations": {
        "response_style": "reflective",
        "sandhi_response": "The expectations of our families can feel like a heavy anchor. But your worth as a child and a person is not a transaction tied to grades.",
        "wisdom_theme": "self_worth",
        "tone": "soft",
        "length": "medium"
    },
    "no_friends": {
        "response_style": "reflective",
        "sandhi_response": "Being surrounded by people yet feeling invisible is a very specific pain. It takes time to find those who speak the same emotional language.",
        "wisdom_theme": "connection",
        "tone": "gentle",
        "length": "medium"
    },
    "exhaustion": {
        "response_style": "calming",
        "sandhi_response": "When your energy is at zero, your mind will catastrophize everything. Rest is not something you earn; it is something you need to survive.",
        "wisdom_theme": "self_care",
        "tone": "warm",
        "length": "medium"
    },
    "rumination": {
        "response_style": "reflective",
        "sandhi_response": "Overthinking often feels like preparation, but after a point it simply becomes emotional exhaustion. Let's ground ourselves in this exact moment.",
        "wisdom_theme": "awareness",
        "tone": "calm",
        "length": "medium"
    }
}

def procedural_response(input_id, subcategory):
    # Default fallback response
    default_data = {
        "response_style": "reflective",
        "sandhi_response": "I hear the distress in your words. When we carry this emotional weight, everything feels magnified. You are not alone, and we can navigate this one step at a time.",
        "wisdom_theme": "mindfulness",
        "tone": "gentle",
        "length": "medium"
    }
    
    match = RESPONSE_DATABASE.get(subcategory, default_data)
    
    return {
        "response_id": f"rsp_{input_id.split('_')[-1]}",
        "input_id": input_id,
        "response_style": match["response_style"],
        "sandhi_response": match["sandhi_response"],
        "wisdom_theme": match["wisdom_theme"],
        "tone": match["tone"],
        "length": match["length"]
    }

# ----------------- Execution Main -----------------

inputs_path = r"c:\workflow\sandhi-memory-mapping-dataset\sandhi-emotional-intelligence-dataset\sandhi_dataset_pipeline\processed_data\inputs.json"
outputs_dir = r"c:\workflow\sandhi-memory-mapping-dataset\sandhi-emotional-intelligence-dataset\sandhi_dataset_pipeline\outputs"

print("Beginning Sandhi Response Generation Pipeline...")

with open(inputs_path, "r", encoding="utf-8") as f:
    inputs_data = json.load(f)

responses_data = []

if HAS_GENAI and not is_placeholder:
    print("Valid Gemini API Key found. Generating responses via Gemini 2.5 Flash...")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    for i, inp in enumerate(inputs_data):
        inp_id = f"fof_{i+1:03d}"
        
        prompt = f"""
        Act as 'Sandhi', an extremely advanced, wise, and empathetic emotional support AI. 
        Your tone should be calm, therapeutic, soft, and insightful.

        Generate a counseling response to the following user input statement.

        Return ONLY a raw valid JSON block. DO NOT use markdown code fence formatting.

        Format:
        {{
          "response_style": "counseling style (e.g. grounding, reflective, calming)",
          "sandhi_response": "the empathetic, wise counseling response itself (keep it to 2 highly potent sentences)",
          "wisdom_theme": "philosophy/wisdom theme (e.g. detachment, self_worth, awareness, connection)",
          "tone": "counseling tone (e.g. calm, soft, gentle, warm)",
          "length": "medium"
        }}

        User Input:
        "{inp['user_input']}"
        """
        
        try:
            response = model.generate_content(prompt)
            cleaned = response.text.replace("```json", "").replace("```", "").strip()
            
            # Extract raw json
            import re
            json_match = re.search(r'\{.*\}', cleaned, re.DOTALL)
            if json_match:
                cleaned = json_match.group(0)
                
            res_obj = json.loads(cleaned)
            res_obj["response_id"] = f"rsp_{i+1:03d}"
            res_obj["input_id"] = inp_id
            
            responses_data.append(res_obj)
            print(f"[{i+1}/{len(inputs_data)}] Generated response via Gemini.")
        except Exception as e:
            print(f"[{i+1}/{len(inputs_data)}] AI API error: {e}. Falling back to procedural counselor.")
            responses_data.append(procedural_response(inp_id, inp["subcategory"]))
else:
    print("Using Rule-Based Empathetic Counseling Generator Fallback...")
    for i, inp in enumerate(inputs_data):
        inp_id = f"fof_{i+1:03d}"
        responses_data.append(procedural_response(inp_id, inp["subcategory"]))
        print(f"[{i+1}/{len(inputs_data)}] Generated response via fallback counselor.")

os.makedirs(outputs_dir, exist_ok=True)
output_path = os.path.join(outputs_dir, "responses.json")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(responses_data, f, indent=2, ensure_ascii=False)

print(f"\nResponse Generation Complete! Saved {len(responses_data)} Sandhi responses to {output_path}")
