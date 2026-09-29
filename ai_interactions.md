# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->
I asked the AI coding assistant to add a Guess History sidebar to my streamlit application. The sidebar should display each previous guess and whether it was Too High, Too Low, or Correct. I asked the agent to write the code without modifying the previous one.

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->
The agent modified `app.py` to implement the Guess History feature using Streamlit session state. It performs the following:
- Added history list to `st.session_state`.
- Recorded each submitted guess and its result.
- Added a Guess history section to the sidebar.
- Cleared the history when starting a new game.
- Ran the existing pytest tests.

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->
I manually tested the application in Streamlit to verify that guesses appeared in the sidebar and the history was cleared when starting a new game. During testing, I encountered a type error caused by the secret number being converted into string and number. So I asked the AI assistant to correct the underlying issue.
---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

**Prompt Used**:

Challenge 1: Review my `logic_utils.py` and `tests/test_game_logic.py` files for this. Identify 3 potential edge cases that could cause problems such as negative, decimals, or very large values and explain me why each of them is worth testing and generate pytest tests for them. Do not modify or fix any of my code only suggest the edge cases and tests

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
