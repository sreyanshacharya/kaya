#input the current state.json + feedback

#form of output
# out = {"action_required" : True/False,
#        "action_type" : name of action in strings

def decide_action(state):
  progress = state.get("progress", {})

  changew = state["current_plan"]["exercise"].get("change", "")
  energy = progress.get("reported_energy_level", "")
  hunger = progress.get("overall_hunger", "")
  ans=[]
  flag=False

#workout

  if changew == "True":
     ans.append({
        "action_required" : True,
        "action_type" : "change_workout",
        "reason" : "user requested complete change of workout plan"
     })
     flag=True

  if energy == "low":
    ans.append({
      "action_required" : True,
      "action_type" : "reduce_w_intensity",
      "reason" : "user reported low energy"
    })
    flag=True
  
  if energy == "high":
    ans.append({
        "action_required": True,
        "action_type": "increase_w_intensity",
        "reason": "user reported high energy"
    })
    flag=True

#diet
  if hunger == "high":
      ans.append({
          "action_required": True,
          "action_type": "modify_diet_more_food",
          "reason": "User reported high hunger"
      })
      flag=True

  if hunger == "low":
      ans.append({
          "action_required": True,
          "action_type": "modify_diet_less_food",
          "reason": "User reported low hunger"
      })
      flag=True
  if flag==False :
    ans.append({
        "action_required": False,
        "action_type": "do_nothing",
        "reason": "No adjustment needed"
    })
  return ans
  
  