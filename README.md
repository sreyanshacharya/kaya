# Introducing Kaya,

> Your lifelong companion to keep diabetes at bay :>

## What is Kaya?

Kaya is an Agentic System that provides adaptive, non-clinical lifestyle guidance for fitness and health goals, specifically for people already diagnosed with diabetes. Instead of offering static plans or one-shot recommendations, Kaya operates as a long-term agent that:

1. continuously adapts to user habits and feedback
2. revisits recommended plans over time
3. makies safe and constraint-friendly decisions that prioritize long-term consistency

> Note - Kaya does not give medical diagnosis or treatment advice. It strictly operates at a lifestyle-support level.

---

## What is Kaya Solving?

Lifestyle management for people diagnosed diabetes is not a one-time optimization problem. It is a continuous process involving:

- fluctuating energy levels
- missed workouts
- changing habits and constraints

Most existing systems solve this by giving :

- static excercise plans
- generic diet advice
- single-turn recommendations

These approaches fail when users deviate from the plan - which happens more often than not.

Kaya is designed to handle this uncertainty by reasoning and adapting over time, rather than sticking to fixed outputs.

---

## Why an agentic System?

This problem cannot be solved effectively with a single ML model or a one-shot LLM call.

Kaya is implemented as an autonomous agent because:

- goals are long-term and evolving
- user behavior is noisy and unpredictable
- plans must adapt based on observed outcomes
- decisions must fall within constraints

The focus is how the system acts and evolves over time, not on model performance alone.

---

## System Overview

At a high level, Kaya operates as a goal-driven control loop with explicit memory and decision-making.

Observe → Decide → Generate → Apply → Persist

- The agent observes daily user feedback
- Decides whether change in any plan is needed
- Uses an LLM to generate an updated plan only if required
- Applies safe, validated changes
- Persists state till the next iteration

---

## Kaya's Architecture

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

---

## Current Implementation Status

- Core agent loop implemented and functional
- Deterministic decision-making logic validated without LLM dependency
- LLM plan generation integrated with strict output validation
- Streamlit-based UI under active development

The current focus is on correctness, clarity and agentic behaviour rather than feature breadth.

---

## Limitations & Future Work

- No wearable or sensor data integration yet
- Limited action space by design
- No long-term learning beyond state-based persistence
- UI is intentionally minimal as of this state.

These limitations are intentional to prioritize clean agent design, safety and ease of use, while ensuring scope for future developments.

---

## Running the System

To run Kaya, follow these steps :

1. Clone the repository using :

- git clone https://github.com/sreyanshacharya/kaya.git

2. Install the required libraries :

- pip install -r requirements.txt

3. Setup the .env file, ensuring GEMINI_API_KEY is present.

4. Run the app :

- streamlit run app.py

Voila!

---
