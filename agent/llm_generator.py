from google import genai
import json
from jsonschema import validate, ValidationError
from datetime import datetime

client = genai.Client()

def llm_generate(state, action=""):
    with open("teststate.json", "r") as f:
        state = json.load(f)

    goal = state["goal"].get("primary_objective", "")
    gtime = state["goal"].get("time_horizon_days", "")


    OUTPUT_SCHEMA = {
  "type": "object",
  "properties": {
    "current_plan": {
      "type": "object",
      "properties": {
        "diet_plan": {
          "type": "object",
          "properties": {
            "carbs": {
              "type": "string",
              "description": "Description of carbohydrate intake (e.g. low, moderate, complex carbs focus)"
            },
            "fats": {
              "type": "string",
              "description": "Description of fat intake (e.g. healthy fats, limited oils)"
            },
            "protein": {
              "type": "string",
              "description": "Protein strategy (e.g. adequate plant protein)"
            },
            "fiber": {
              "type": "string",
              "description": "Fiber guidance (e.g. high fiber vegetables)"
            },
            "other_macronutrients": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Any additional nutrition notes (micronutrients, hydration, etc.)"
            }
          },
          "required": [
            "carbs",
            "fats",
            "protein",
            "fiber",
            "other_macronutrients"
          ],
          "additionalProperties": False
        },
        "exercise": {
          "type": "object",
          "properties": {
            "duration_minutes": {
              "type": "number",
              "minimum": 0,
              "description": "Exercise duration in minutes"
            },
            "routine": {
              "type": "string",
              "description": "Type of exercise routine (e.g. walking, stretching)"
            },
            "change": {
              "type": "string",
              "description": "What changed compared to the previous plan (e.g. reduced duration)"
            }
          },
          "required": [
            "duration_minutes",
            "routine",
            "change"
          ],
          "additionalProperties": False
        }
      },
      "required": [
        "diet_plan",
        "exercise"
      ],
      "additionalProperties": False
    }
  },
  "required": [
    "current_plan"
  ],
  "additionalProperties": False
}


    prompt = f"""
    You are assisting an agentic system in helping the user achieve this goal : {goal}
    There are {gtime} days left.

    Your task:

    Generate a new json that corresponds to the action : {action}

    Generate ONLY valid JSON matching the schema below.
    Do NOT include markdown, comments, or explanations.
    Do NOT add extra fields.
    Do NOT give medical diagnosis and treatment advice.

    Schema:
    {json.dumps(OUTPUT_SCHEMA, indent=2)}

    User profile:
    {json.dumps(state["user_profile"], indent=2)}

    Constraints:
    {json.dumps(state["constraints"], indent=2)}

    Goal:
    {json.dumps(state["goal"], indent=2)}
    """

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt)
    raw_output = response.text.strip()

    try:
        plan_update = json.loads(raw_output)
        validate(instance=plan_update, schema=OUTPUT_SCHEMA)
    except (json.JSONDecodeError, ValidationError) as e:
        raise RuntimeError("Invalid LLM output") from e

    return plan_update

# 📄 Load state

# state["current_plan"] = plan_update["current_plan"]
# state["agent_meta"].update(plan_update["agent_meta"])
# state["agent_meta"]["last_updated"] = datetime.now().isoformat()


# with open("teststate.json", "w") as f:
#     json.dump(state, f, indent=2)

# print("✅ State updated successfully")
