#goal satisfaction reached
#time horizon reached
#return :
#true to stop
#false to continue

def should_terminate(state):
    progress = state.get("progress", {})
    goal = state.get("goal", {})

    # adherence = progress.get("adherence_score", 0.0)
    # threshold = goal.get("success_threshold", 1.0)

    # return adherence >= threshold

    passtime = progress.get("day_count", 0)
    goaltime = goal.get("time_horizon_days", 0)

    return passtime>=goaltime

