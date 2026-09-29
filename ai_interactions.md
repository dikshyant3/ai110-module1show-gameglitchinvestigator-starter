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
| Decimal guess| Challenge 1 prompt| check_guess(12.9, 50) should return ("Too Low", "📈 Go HIGHER!")| Yes | Tests whether the comparison logic handles a decimal value correctly. | 
| Negative guess| Challenge 1 prompt| check_guess(-10, 50) should return ("Too Low", "📈 Go HIGHER!")| Yes |  Tests whether the comparison logic can handle negative number |
| Very Large guess| Challenge 1 prompt| check_guess(10**1000, 50) should return ("Too High", "📉 Go LOWER!")| Yes | Tests whether the comparison logic can handle an extremely large integer without failing. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
Inspect the logic_utils.py and add professional-grade docstrings to every function in this file and do not change any behavior of the function and use consistent docstring throughout the file. After doing this, show me what you have changed.
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
logic_utils.py:37:80: E501 line too long (87 > 79 characters)
logic_utils.py:41:80: E501 line too long (119 > 79 characters)
logic_utils.py:77:80: E501 line too long (87 > 79 characters)
app.py:56:1: E305 expected 2 blank lines after class or function definition, found 1
app.py:123:80: E501 line too long (174 > 79 characters)
app.py:128:80: E501 line too long (92 > 79 characters)
app.py:147:80: E501 line too long (89 > 79 characters)
app.py:152:80: E501 line too long (89 > 79 characters)


```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->
I have installed pycodestyle for verifying or checking the linting error. Then I asked my AI agent to resolve those error using the below prompt.
```
Please review the following pycodestyle output in the above txt file and fix these PEP8 issues do not modify any code logic, function names, values and all. After making the changes, please explain each formatting changes you have made
```
---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | Claude| Copilot |
| **Response summary** | Fixed the reversed hints and added try/except TypeError handling with string comparison as well | Fixed the reversed hints using a simple structure and added string comparison as well but there was no sign of try/except |
| **More Pythonic?** | I think it is more complex than necessary for this bug| It is more straightforward and concise for the bug |
| **Clearer explanation?** | Claude explained the issue more clearly by providing the comparison between the guess and secret number and why each hint should be higher or lower. | Copilot gave shorter explanation based on just the corrected conditions|

**Which did you prefer and why?**

<!-- Your conclusion -->
I preferred Copilot's code because it was simpler and direct but Claude was more defensive and its explantion was clear so it can also be used for safer AI solutions and when proper security is required.
