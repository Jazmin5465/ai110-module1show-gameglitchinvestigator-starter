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

- [X] Describe the game's purpose.
This number guessing generates a secret number falling into a range depending on difficulty level. The user then has a limited amount of guesses to try to correctly guess the secret number. The game will optionally give hints if a guess was lower or higher than the secret number.
- [X] Detail which bugs you found.
A few of the bugs I found include function logic not being in the right file, a user's ability to guess a number outside of the designated range, ability to guess non-integer numbers, and the difficulty ranges did not line up with the correct difficulty modes.
- [X] Explain what fixes you applied.
With the help of AI, we moved the function logic from app.py into logic_utils.py. I also had the AI generate input verification to ensure that the user's guess was a valid guess in the right range and data type before counting it as one of their attempts. Lastly, I had the AI find the lines of code where difficulty levels assigned ranges and made sure that they were correctly modified as well as updating correctly in the UI. We checked these fixes by adding tests for different scenarios that were ran using pytest.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 9.5
2. Game returns "Enter a whole number (no decimals).
3. User enters a guess of 45
4. Game returns "Go LOWER!"
5. Score and number of attempts updates after every valid/in-range guess
6. Game ends after correct guess or user runs out of attempts

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
========================================== test session starts ===========================================
platform win32 -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\jazmi\OneDrive\Codepath\Proj 1\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 9 items                                                                                         

tests\test_game_logic.py .........                                                                  [100%]

=========================================== 9 passed in 0.18s ============================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
