# Python Quiz Game

A terminal quiz game with 10 tech questions, instant feedback,
shuffled question order, and a final grade. Written in pure Python -
no packages to install.

## Features

- 10 multiple-choice questions about computers and programming
- Questions shuffle every round, so replays feel fresh
- Input validation (only A-D accepted)
- Score, percentage, and a friendly grade at the end
- Replay loop - press `y` to go again

## Run it

```bash
python3 quiz.py
```

Works on any system with Python 3.6+ (Windows, macOS, Linux).

## Sample

```
========================================
   Welcome to the Tech Quiz Game!
========================================

Question 1/10: How many bits are in one byte?
  A) 4
  B) 16
  C) 8
  D) 32
Your answer (A-D): C
Correct!
```

## Add your own questions

Open `quiz.py` and append to the `QUESTIONS` list:

```python
{
    "question": "Your question here?",
    "choices": ["first", "second", "third", "fourth"],
    "answer": 2,   # index of the correct choice (0-3)
},
```

## Testing status

Tested by playing full rounds on Python 3.10 - scoring, validation,
and the replay loop all work as expected.
