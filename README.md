# Introducing Kaya,

> Your lifelong companion to keep diabates at bay :>

## What is Kaya?

Kaya is an Agentic System that provides adaptive, non-clinical lifestyle guidance for fitness and health goals, specifically for people with diabetes. It does so by :

1. continuously adapting to user habits and taking feedbacks
2. revising it's recommended plans over time
3. making safe and constraint-friendly decisions
4. prioritizing consistency of the user over rigid optimization

Note - Kaya does not give medical diagnosis or treatment advice. It strictly operates at a lifestyle-support level.

---

## What is Kaya Solving?

Lifestyle management for people diagnosed diabetes is not a one-solution problem. It is a lifelong evolution of daily decisions, fluctuating energy levels, missed workout sessions and changing constraints.
Current systems provide :

- static excercise plans
- generic diet advice
- everyday suggestions that aren't personalised

These systems fail to adapt to the everyday deviations from the plans, which is the normal case for almost everyone. This is where Kaya makes a difference.

Being an Agentic System, it gains an edge over regular ML models and single-turn LLMs as :

- It's goals are long-term and evolving
- It is designed to adapt to user behavior that is typically uncertain and noisy
- It's plans adapt based on feedback
- It always operates under constraints defined by the user

---

## What is it made of?

kaya is built from some components designed to work as a synchronised unit.

### 1. User Interface
Kaya's Interface is designed using Streamlit. 
The UI is responsible only for :
- Displaying active plans
- Accepting user inputs and feedbacks
- Showing Kaya’s recommendations and reasoning

### 2. State File
This is the memory of the Kaya. A JSON file which contains all the 
- user data 
- Goal : This data is static and the agent will follow the plan and execution until the user reaches the end goal.
- constraints
- active plans
- current progress 
- History of changes made(upto a limit).
