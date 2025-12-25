#input the current state.json + feedback

#form of output
# out = {"action_required" : True/False,
#        "action_type" : name of action in strings

def decide_action(state):
  progress = state.get("progress", {})
  
  changew = state["current_plan"]["exercise"].get("change", "")
  energy = progress.get("reported_energy_level", "")
  hunger = progress.get("overall_hunger", "")

#workout

  if changew == "True":
     return{
        "action_required" : True,
        "action_type" : "change_workout",
        "reason" : "user requested complete change of workout plan"
     }

  if energy == "low":
    return {
      "action_required" : True,
      "action_type" : "reduce_w_intensity",
      "reason" : "user reported low energy"
    }
  
  if energy == "high":
    return {
        "action_required": True,
        "action_type": "increase_w_intensity",
        "reason": "user reported high energy"
    }

#diet
  if hunger == "high":
      return {
          "action_required": True,
          "action_type": "modify_diet_more_food",
          "reason": "User reported high hunger"
      }

  if hunger == "low":
      return {
          "action_required": True,
          "action_type": "modify_diet_less_food",
          "reason": "User reported low hunger"
      }

  return {
      "action_required": False,
      "action_type": "do_nothing",
      "reason": "No adjustment needed"
  }
  
  