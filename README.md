# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

During this project, I used LLMs such as Claude and Copilot to help identify, understand, and fix bugs in the guessing game. I learned that it is important to understand the suggested changes instead of accepting them without checking the code. I used pytest to verify the guessing logic and difficulty ranges, and I manually tested the New Game behavior in Streamlit. This helped me understand the difference between testing a function directly and testing how that function is used by the application.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step --> The user selects a difficulty level and starts a new game.
2. <!-- Describe this step --> The game selects a random secret number within the difficulty group.
3. <!-- Describe this step --> The user enters a guess of 40.
4. <!-- Describe this step --> If the secret number is 50, the game returns "Too Low" and tells the user to go higher.
5. <!-- Add more steps as needed --> The user enters a guess of 60.
6. The game returns "Too High" and tells the user to go lower.
7. The user enters the correct guess of 50.
8. The game returns "Win" and displays the correct message.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
Output:
===================================== test session starts =====================================
platform darwin -- Python 3.13.13, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/dikshyant/codepath-ai110/Labs/Game-Glitch/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 6 items                                                                             

tests/test_game_logic.py ......                                                         [100%]

====================================== 6 passed in 0.02s ======================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

Challenge 1 pytest result

========================================================== test session starts ===========================================================
platform darwin -- Python 3.13.13, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/dikshyant/codepath-ai110/Labs/Game-Glitch/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 9 items                                                                                                                        

tests/test_game_logic.py .........                                                                                                 [100%]

=========================================================== 9 passed in 0.02s ============================================================
