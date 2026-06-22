# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  One bug was that the new game button didn't reset the message "Start a new game to play again" as well as not updating the number of attempts left. Another bug was that changing difficulty level is supposed to update the range in which users can guess as well as number of attempts and the message being displayed does not reflect this change.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  1.5  | "must be whole #" | "go lower"      | none                   |
|  -90  | "out of bounds"   | "go lower"      | none                   |
|  50   | "go lower"        | "go higher"     | none                   |
|  Hard | "Range 1-100"     | "Range 1-50"    | none                   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude AI.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

When it came to editing the difficulty ranges and the corresponding display message, the AI correctly identified that part of the message was hardcoded instead of containing the variables that change based on difficulty level. I verified the result by changing the difficulty in the web app and seeing if the message changed to reflect the range designated for each level of difficulty.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

At first the AI thought that the "Too high/too low" issue was due to a string conversion. I verified by looking at the line of code that it mentioned that the conversion was happening in and saw that it was mistaking the streamlit method/variable names for a conversion. I redirected it by specifying to look at the if statement where it then found that the hint text itself had mismatched outcomes.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

To tell if a bug was really fixed, I ran the app.py file to see the game in action and click around to see if it responded the way I intended it too. I also manually went through the code and looked at the lines that the AI said it targeted to see if the changes it made were correct and neccessary.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

Using pytest, I ran a test to check if the guess was above or below the range and it verifies if it asserts the correct error message indicating for the guess to be in the correct range. It proved that the code correctly shows a message for the user to try guessing again.

- Did AI help you design or understand any tests? How?

I asked the AI to write the test cases by considering all scenarios (in range, out of range, and decimals vs whole numbers). It helped automate the proccess of writing the tests. It was also able to run the file and verify whether the tests passed on their own while also giving me feedback and explanations on the sample numbers it used with their expected outcome.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
