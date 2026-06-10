# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

**Initial Prompt:**
```
Come up with three potential edge cases that can still break the game. 
Generate pytest cases to verify the game handles them properly.
```

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Score going negative | "What happens if a player gets multiple 'Too Low' penalties in a row?" | test_score_cannot_go_negative: Tests that each penalty deducts 5 points and verifies behavior at 0 and negative ranges | Yes | Critical to validate game doesn't crash when score approaches/reaches zero or negative values; prevents undefined behavior in scoring system |
| Boundary guess at minimum | "How does the game handle guessing at the extreme boundaries like 1 or 100?" | test_boundary_guess_at_minimum: Tests correct/incorrect guesses at value 1 and type mismatch handling | Yes | Boundary values often expose comparison logic bugs; minimum value (1) is easiest edge case to miss in testing |
| Boundary guess at maximum | Same as above | test_boundary_guess_at_maximum: Tests correct/incorrect guesses at value 100 and type mismatch handling | Yes | Maximum value (100) is the other common boundary; ensures symmetry in comparison logic for both extremes |
| Winning on final attempt | "What score should a player get if they win on the absolute last allowed attempt?" | test_winning_on_final_attempt: Tests winning on attempts 5 and 8 to verify score calculation reaches minimum of 10 | Yes | Critical path: validates game transitions correctly when player wins at the exact attempt limit; ensures scoring formula doesn't break at limits |

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
