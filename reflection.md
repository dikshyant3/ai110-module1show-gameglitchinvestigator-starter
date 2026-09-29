# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  When I first ran the game, the user interface worked fine and I was able to enter guesses, but I noticed some incorrect logic. One of the first bugs I found was the hints were backwards. For instance, when the secret number was 39 and I guessed 38, the game identified my guess as too low which is correct but the message was to "Go Lower" instead of "Go Higher". Another problem I noticed was the secret number not being in the range with the difficulty level selected. Third one was with the resetting of the game state. For example, When I made few guesses and clicked New Game, the score and my previous guess history were still there.
 
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Secret=39, Guess=38 |Output should display "Too Low" and tell the player to guess Higher | Output displays "Too Low" but told the player to go Lower|No console error |
|Easy difficulty, click New Game |New secret should be between 1 and 20 |New secret is between 1 and 100 |No console error |
|Play several guesses, then click New Game |Score and history should reset for the new game |Previous score is still showing after starting a new game |No console error |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used  Copilot and Claude for this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
An AI suggestion which I accepted was correcting the reversed High/Low hints. I accepted this suggestion because it separated the actual logic from the user interface and fixed the bug. I verified the change using pytest and by testing the game in the Streamlit.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
An AI suggestion I did not accept as written was adding the code to convert the secret from a string to integer inside check_guess() function. I thought that the issue was not related with the bug I was solving so I avoided it and focused on the selected hint-direction bug only.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

For the first bug, I tested check_guess() with a correct guess, a guess too high, and a guess too low. The correct guess returned "Win" with the correct message. And then I checked it with a guess of 60 with a secret of 50 returned "Too high" with "Go lower" as message and a guess of 40 with a secret of 50 returned "Too low" with "Go higher". Finally, I ran the pytest tests and confirmed that they passed. For the second bug, I tested the difficulty ranges using pytest. The tests verified that Easy returns 1-20, Normal returns 1-100 and Hard returns 1-50. I then tested the New Game for each difficulty level to verify that the generated secret matched the selected difficulty range. Finally, I ran the test cases for all the bugs I found and it passed all the six cases. Yes, AI helped me design the test by suggesting the test cases for both bugs. It helped me understand the second bug testing is not enough only through the pytest so I also manually tested the New Game behavior in the application.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would explain Streamlit reruns the Python script from the beginning again whenever the user interacts with the app. Because of this, normal variables can reset. Session state saves important information, like the secret number, game history and score so that it stays available when the app runs again.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  - One habit I want to reuse in future labs or projects is running the tests after making a code change instead of assuming the code fix I have done works completely normal. I also want to review the suggestions of the AI and verifying them myself before accepting them automatically.

- What is one thing you would do differently next time you work with AI on a coding task?
  - I think providing more specific information about the bug and the code I am working on rather than directly asking for a fix. Like I have already mentioned, I will also consider validating the suggested change rather than accepting it automatically.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - One of the most important thing this project taught me is that AI-generated code can be useful for finding and fixing bugs but it should still be verified by the developer. Secondly, I think I should treat the suggestions AI provides as recommendations and then using my own reasoning to decide whether they are appropriate.
