import google.generativeai as genai
import json
from jsonschema import validate, ValidationError
from datetime import datetime

model = genai.GenerativeModel("gemini-2.5-flash")

# 📄 Load state
with open("teststate.json", "r") as f:
    state = json.load(f)

OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "current_plan": {
            "type": "object",
            "properties": {
                "diet_plan": {
                    "type": "object",
                    "properties": {
                        "approach": {"type": "string"},
                        "guidelines": {
                            "type": "array",
                            "items": {"type": "string"}
                        }
                    },
                    "required": ["approach", "guidelines"]
                },
                "exercise": {
                    "type": "object",
                    "properties": {
                        "duration_mins": {"type": "number"},
                        "intensity": {"type": "string"},
                        "routine": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "frequency": {"type": "number"}
                    },
                    "required": ["duration_mins", "intensity", "routine", "frequency"]
                },
                "notes": {"type": "string"}
            },
            "required": ["diet_plan", "exercise", "notes"]
        },
        "agent_meta": {
            "type": "object",
            "properties": {
                "last_reasoning_summary": {"type": "string"},
                "last_action_taken": {"type": "string"}
            },
            "required": ["last_reasoning_summary", "last_action_taken"]
        }
    },
    "required": ["current_plan", "agent_meta"]
}

prompt = f"""
You are a diabetic fitness planning agent.

Your task:
Generate ONLY valid JSON matching the schema below.
Do NOT include markdown, comments, or explanations.
Do NOT add extra fields.

Schema:
{json.dumps(OUTPUT_SCHEMA, indent=2)}

User profile:
{json.dumps(state["user_profile"], indent=2)}

Constraints:
{json.dumps(state["constraints"], indent=2)}

Goal:
{json.dumps(state["goal"], indent=2)}
"""

response = model.generate_content(prompt)
raw_output = response.text.strip()

try:
    plan_update = json.loads(raw_output)
    validate(instance=plan_update, schema=OUTPUT_SCHEMA)
except (json.JSONDecodeError, ValidationError) as e:
    raise RuntimeError("Invalid LLM output") from e

state["current_plan"] = plan_update["current_plan"]
state["agent_meta"].update(plan_update["agent_meta"])
state["agent_meta"]["last_updated"] = datetime.now().isoformat()


with open("teststate.json", "w") as f:
    json.dump(state, f, indent=2)

print("✅ State updated successfully")
