#init (once only)

#agent contacts - action dec 
# -> agent picks from action 
# -> action executed from actions.py
# -> state updated in the actions.py
# -> displayed back to frontend

import json
from pathlib import Path
from datetime import datetime

from .actiondec import decide_action
from .actions import ACTION_MAP

STATE_PATH = Path(__file__).parent.parent / "state.json"

def load_state() : 
  with open(STATE_PATH, "r") as f:
    return json.load(f)

def save_state(state):
  with open(STATE_PATH, "w") as f:
    json.dump(state, f, indent=2)


def agent_step():
  #STATE
  state = load_state()

  #DECISION
  decision = decide_action(state)
  action_type = decision["action_type"]
  reason = decision["reason"]

  #ACTION TAKEN
  if decision["action_required"]:
    action_fn = ACTION_MAP[action_type]
    action_fn(state, reason)

  #LOG TO META
  state["agent_meta"]["last_decision"] = action_type
  state["agent_meta"]["last_reasoning_summary"] = reason
  state["agent_meta"]["updated"] = datetime.now().isoformat()

  save_state(state)

  return state

