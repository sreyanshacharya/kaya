from datetime import datetime

def log_action(state, action_type, reason):
  state["history"].append({
      "timestamp" : datetime.now().isoformat(),
      "action_taken" : action_type,
      "reason" : reason
    })

def do_nothing(state, reason):
  log_action(state, "do_nothing", reason)

def reduce_w_intensity(state, reason):
  exercise = state["current_plan"]["exercise"]
  old = exercise.get("duration_minutes", 0)
  exercise["duration_mins"] = max(10, old-5)

  log_action(state, "reduce_w_intensity", reason)

def increase_w_intensity(state, reason):
  exercise = state["current_plan"]["exercise"]
  old = exercise.get("duration_minutes", 0)
  exercise["duration_mins"] = old + 10

  log_action(state, "increase_w_intensity", reason)

def modify_diet_more_food(state, reason):
  #llm magic
  diet = state["current_plan"]["diet_plan"]
  diet["guidelines"].append("more food quantity requested")
  
  log_action(state, "modify_diet_more_food", reason)

def modify_diet_less_food(state, reason):
  #llm magic again
  diet = state["current_plan"]["diet_plan"]
  diet["guidelines"].append("less food quantity requested")

  log_action(state, "modify_diet_less_food", reason)

def change_workout(state, reason):
  #llm changes entire workout
  log_action(state, "change_workout", reason)


ACTION_MAP = {
  "do_nothing": do_nothing,
  "reduce_w_intensity": reduce_w_intensity,
  "increase_w_intensity": increase_w_intensity,
  "modify_diet_more_food": modify_diet_more_food,
  "modify_diet_less_food": modify_diet_less_food,
  "change_workout" : change_workout
}
