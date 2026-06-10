# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The game looked like it had a very simple menu. It allows a user to input a number, submit the guess, create a new game, decide if they want to show a hint or not, and change the difficulty. There is also a developer debug info section that can be opened. It provides the hidden number, attempts, score, difficulty, and history of guesses.

  Two major bugs I found were that the hints were backwards and the new game button does not work. When your guess is wrong, the game provides the opposite hint. Also when trying to start a new game, it will not actually start a new game. It just resets the number of attempts only. One more bug I found was that the number of attempts was actually off by one. Normal difficulty provides users 8 attempts, but only actually counts 7 attempts.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| New Game Button | Starts a new game | Reset attemps, but would not allow new inputs | none |
| 75 | Hints should be accurate | Provides inaccurate hints about the answer | none |
| 50 | Provide accurate number of attempts | Shows result before last attempt is used | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI tool I used on the project was Copilot.

One correct AI suggestion was a fix for the incorrect hints saying that it would give the opposite hint to the user. It provided the logic behind it and how to fix the issue. I verified it by testing it on the game and using pytest cases. The AI was able to correct it easily and provide correct results.

One incorrect AI suggestion was a fix for the number of attempts a user has left. It was able to fix the number of attempts left, but it did not fix the attempts left displayed. After repeated prompted, the AI was eventually able to fix the displayed attempts left while also keeping an accurate count of attempts. I verified these results by repeatedly guessing on the game to view the attempts used and were remaining.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed by ensuring the generated test cases all passed after a bug implemented. I did a double check by also trying to recreate the bug on the game and ensuring it wouldn't occur again.

One test I ran was just checking the hints on the game through repeated guessing. Before any changes, I wanted to identify if there was a pattern to the incorrect hints. After I discovered it actually provided opposite hints (so it would say higher if it was actually lower for example), and I went to write a fix using the AI. Afterward, I went to test the out if the hints were correct or incorrect now. I did this by inputting guesses that were lower, higher, and the secret number to make sure correct outputs occured.

AI helped a lot with identifying where the bug occured and why it was happening. While I understood the bug itself, AI was extremely helpful at showing me where the bug was happening and why it was happening. It was like this for all the bugs, and it helped show that my tests were working as they were based off the AI explaination. Its explainations played a big part in my understanding of the tests.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns are basically when Streamlit reruns the entire script over again when it occurs. It stops executing anything else and reruns the script from scratch. Session state is any values or memory that is saved for a user session. So when a rerun occurs, anything stored in the session state is carried over to the rerun.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I definitely liked how the instructions had us use AI. It forced use to be precise with how we were approaching any bugs before fixing them, and I want to keep this up. Using AI in a way where it helps us identify bugs, and then fix it instead of just asking it to fix the code provides a lot more clarity. I want to keep this up.

I tried to be specific with my prompting, but the AI was still struggling to fix a bug at times. It would mess with the page or not take things into account despite understanding what the bug was. I need to be even more specific next time in my prompting in order to avoid these issues. This is what I want to do differently.

This project made me realize how badly my prompting was as you could get much more out of AI. Instead of just asking for a quick fix, ask it to explain and locate the bugs first, and then fix so the AI generated code makes more sense.