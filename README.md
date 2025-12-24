# Introducing Kaya,

> Your lifelong companion to keep diabates at bay :>

## What is Kaya?

Kaya is an Agentic System that provides adaptive, non-clinical lifestyle guidance for fitness and health goals, specifically for people with diabetes. It does so by :

1. continuously adapting to user habits and taking feedbacks
2. revising it's recommended plans over time
3. making safe and constraint-friendly decisions
4. prioritizing consistency of the user over rigid optimization

> Note - Kaya does not give medical diagnosis or treatment advice. It strictly operates at a lifestyle-support level.

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

kaya is built with 5 core components which are designed to work as a synchronized and tightly coupled unit. Each layer has a clearly defined responsibilty which is not compromised.

### 1. User Interface
Kaya's Interface is designed using Streamlit. 
The UI is responsible only for :
- Displaying active plans and the current progress
- Accepting user inputs and feedbacks
- Presenting Kaya’s recommendations along with a detailed reasoning

### 2. State File
This file is the memory of Kaya. This is implemented as a single JSON file which contains everything the agents needs to fulfill it's purpose. This contains : 

- user data 
- Goal : This data is static and the agent will follow the plan and execution until the user reaches the end goal.
- constraints
- active plans
- current progress 
- History of changes made(upto a limit).

Kaya reads from and writes to this file on every iteration. This ensures transparency, debuggability, and auditability.

### 3. Action Layers
These are the explicit python functions that define everything Kaya is allowed to do. These can be :

- changing the intensity or the plans of the workouts
- Diet modifications
- Doing nothing if the feedback is positive

Each action works deterministically on the current state and modifies the state file accordingly. 

### 4. LLM Integrations
Kaya makes exactly one LLM call per loop.
The current version uses Gemini 2.5 Flash.
The LLM inputs are taken form the state JSON file.

Inputs :
- Current plan
- Constraints
- Goal

Outputs : 
- Suggested next actions
- Justifications

> Note : LLM is just an advisior. The desisions are strictly taken by the agent.

### 5. Safety Net
The safety Layer is defined between the LLM and the agent's action layer.

It's responsibilities include : 

- Enforcing user-defined medical and safety constraints
- Validating LLM suggestions
- Blocking unsafe or invalid actions 

This acts as a final checkpoint before before any action is excecuted. This ensures reliability even is the LLM's suggestions are uncertain.

