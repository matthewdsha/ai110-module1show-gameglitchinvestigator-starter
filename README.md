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

- The game's purpose is to allow users to guess a secret number. The game will tell them if the number is higher or lower than their guess, and they have to find the number after a certain number of attempts.

- Three bugs I found were that the hints provided were incorrect, the tracking of attempts were off by 1, and the new game button did not work properly.

- I was told to implement two fixes for three of the bugs. I chose to fix the incorrect hints and the number of attempts. I fixed the hints by changing switching them as the AI suggested. It was implemented where the opposite hint would occur. So if a number were lower, it would actually say go lower. I swapped go lower and go higher in the if statements so they would display the correct hints. The other fix for the attempts was a lot more work. The AI had issues keeping the visuals the same while fixing the attempt count. I discovered Streamlit renders pages in the order of the code, so moving things around was not an option for the AI when implementing a fix. There were issues with the number of attempts remaining and displaying the correct value. The AI was eventually able to figure it out and fixed the attempts counter by initializing it at 0 and using button callbacks to update state before the display renders.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 75
2. Game returns "Too High"
3. User enters a guess of 25 -> "Too Low"
4. Score updates correctly after each guess
5. Game ends when user either correctly guesses the secret number or runs out of attempts

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

tests/test_game_logic.py::test_winning_guess PASSED                      [  5%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 11%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 17%]
tests/test_game_logic.py::test_guess_too_high_type_mismatch PASSED       [ 23%]
tests/test_game_logic.py::test_guess_too_low_type_mismatch PASSED        [ 29%]
tests/test_game_logic.py::test_attempt_1_win_score PASSED                [ 35%]
tests/test_game_logic.py::test_attempt_6_win_score PASSED                [ 41%]
tests/test_game_logic.py::test_attempt_limit_exceeded PASSED             [ 47%]
tests/test_game_logic.py::test_too_high_odd_attempt_penalty PASSED       [ 52%]
tests/test_game_logic.py::test_too_high_even_attempt_bonus PASSED        [ 58%]
tests/test_game_logic.py::test_too_low_always_penalty PASSED             [ 64%]
tests/test_game_logic.py::test_attempt_counter_scenario PASSED           [ 70%]
tests/test_game_logic.py::test_display_attempts_left PASSED              [ 76%]
tests/test_game_logic.py::test_score_cannot_go_negative PASSED           [ 82%]
tests/test_game_logic.py::test_boundary_guess_at_minimum PASSED          [ 88%]
tests/test_game_logic.py::test_boundary_guess_at_maximum PASSED          [ 94%]
tests/test_game_logic.py::test_winning_on_final_attempt PASSED           [100%]

============================= 17 passed in 0.07s ==============================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
