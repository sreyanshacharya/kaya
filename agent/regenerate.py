from datetime import datetime
from .llm_generator import llm_generate

def log_action(state, action_type, reason):
  state["history"].append({
      "timestamp" : datetime.now().isoformat(),
      "action_taken" : action_type,
      "reason" : reason
    })

def change_state(state, newplan):
  state["current_plan"] = newplan["current_plan"]
  
def regenerate(state, reason):
  try:
    newplan = llm_generate(state, "regenerate plan completely as the user said : " + reason)
    change_state(state, newplan)
    log_action(state, "manual_regenerate_used", reason)
  except RuntimeError:
    log_action(state, "regeneration_skipped", "LLM Temporarily Unavailable. Current Plan retained.")