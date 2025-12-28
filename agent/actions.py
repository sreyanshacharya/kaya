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

def do_nothing(state, reason):
  log_action(state, "do_nothing", reason)

def reduce_w_intensity(state, reason):
  newplan = llm_generate(state, "reduce workout intensity")
  change_state(state, newplan)

  log_action(state, "reduce_w_intensity", reason)

def increase_w_intensity(state, reason):
  newplan = llm_generate(state, "increase workout intensity")
  change_state(state, newplan)

  log_action(state, "increase_w_intensity", reason)

def modify_diet_more_food(state, reason):
  newplan = llm_generate(state, "modify diet to increase food quantity while keeping calories same")
  change_state(state, newplan)
  
  log_action(state, "modify_diet_more_food", reason)

def modify_diet_less_food(state, reason):
  newplan = llm_generate(state, "modift diet to reduce food quantity while ensuring all nutrient constraints are hit")
  change_state(state, newplan)

  log_action(state, "modify_diet_less_food", reason)

def change_workout(state, reason):
  newplan = llm_generate(state, "change the workout completely")
  change_state(state, newplan)
  log_action(state, "change_workout", reason)


ACTION_MAP = {
  "do_nothing": do_nothing,
  "reduce_w_intensity": reduce_w_intensity,
  "increase_w_intensity": increase_w_intensity,
  "modify_diet_more_food": modify_diet_more_food,
  "modify_diet_less_food": modify_diet_less_food,
  "change_workout" : change_workout
}
