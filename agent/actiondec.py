#input the current state.json + feedback

#form of output
# out = {"action_required" : True/False,
#        "action_type" : name of action in strings

def decide_action(state):
  progress = state.get("progress", {})

  energy = progress.get("reported_energy_level", "")
  hunger = progress.get("overall_hunger", "")
  ans=[]
  flag=False

#workout

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
  
  