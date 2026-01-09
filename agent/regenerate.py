from datetime import datetime
from .llm_generator import llm_generate
from pathlib import Path
import json

STATE_PATH = Path(__file__).parent.parent / "state.json"

def log_action(state, action_type, reason):
  state["history"].append({
      "timestamp" : datetime.now().isoformat(),
      "action_taken" : action_type,
      "reason" : reason
    })

def change_state(state, newplan):
  state["current_plan"] = newplan["current_plan"]


def save_state(state):
  with open(STATE_PATH, "w") as f:
    json.dump(state, f, indent=2)

  
def regenerate(state, reason):
  try:
    newplan = llm_generate(state, "regenerate plan completely as the user said : " + reason)
    change_state(state, newplan)
    log_action(state, "manual_regenerate_used", reason)
    state['agent_meta']['last_reasoning_summary'] = "regenerated plan due to user request."
    state['agent_meta']['last_decision'] = "manually_regenerated"
    state['agent_meta']['updated'] = datetime.now().isoformat()

    save_state(state)
    
  except RuntimeError:
    log_action(state, "regeneration_skipped", "LLM Temporarily Unavailable. Current Plan retained.")
    state['agent_meta']['last_reasoning_summary'] = "regenerated cancelled as LLM was unavailable."
    state['agent_meta']['last_decision'] = "regeneration_skipped"
    state['agent_meta']['updated'] = datetime.now().isoformat()
    save_state(state)