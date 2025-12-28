#run this when running the model.

from agent.agent import agent_step

def main():
  print("Kaya is online.")

  new_state = agent_step()

  print("One agent step completed.")
  print("Action Taken :", new_state["agent_meta"].get("last_action_taken", ""))
  print("Reason for Action :", new_state["agent_meta"].get("last_reasoning_summary", ""))

  print("check json file for changes too.")

if __name__ == "__main__":
  main()