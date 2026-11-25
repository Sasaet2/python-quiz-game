#!/usr/bin/env python3
"""Terminal quiz game with score tracking and instant feedback.

Run with:  python3 quiz.py
"""

import random
import sys

# Each question: the prompt, a list of choices, and the index of the right one.
QUESTIONS = [
    {
        "question": "What does CPU stand for?",
        "choices": ["Central Processing Unit", "Computer Personal Unit",
                    "Central Program Utility", "Core Processing Utility"],
        "answer": 0,
    },
    {
        "question": "Which language is known as the language of the web browser?",
        "choices": ["Python", "JavaScript", "C++", "Java"],
        "answer": 1,
    },
    {
        "question": "How many bits are in one byte?",
        "choices": ["4", "16", "8", "32"],
        "answer": 2,
    },
    {
        "question": "Which of these is NOT a programming language?",
        "choices": ["Python", "HTML", "Kotlin", "Swift"],
        "answer": 1,
    },
    {
        "question": "What does the ESP32 chip have built in?",
        "choices": ["WiFi and Bluetooth", "A camera", "A screen", "A battery"],
        "answer": 0,
    },
    {
        "question": "In Python, which keyword defines a function?",
        "choices": ["func", "function", "def", "define"],
        "answer": 2,
    },
    {
        "question": "What does RAM stand for?",
        "choices": ["Read Access Memory", "Random Access Memory",
                    "Rapid Action Machine", "Remote Array Module"],
        "answer": 1,
    },
    {
        "question": "Which symbol starts a comment in Python?",
        "choices": ["//", "/*", "#", "--"],
        "answer": 2,
    },
    {
        "question": "What is 1024 bytes called?",
        "choices": ["1 megabyte", "1 gigabyte", "1 kilobyte", "1 terabyte"],
        "answer": 2,
    },
    {
        "question": "Which company created the Dart language?",
        "choices": ["Microsoft", "Apple", "Google", "Meta"],
        "answer": 2,
    },
]

LETTERS = ["A", "B", "C", "D"]


def ask_question(question: dict, number: int, total: int) -> bool:
    """Show one question, read the answer, return True if correct."""
    print(f"\nQuestion {number}/{total}: {question['question']}")
    for letter, choice in zip(LETTERS, question["choices"]):
        print(f"  {letter}) {choice}")

    while True:
        raw = input("Your answer (A-D): ").strip().upper()
        if raw in LETTERS[: len(question["choices"])]:
            break
        print("Please enter A, B, C or D.")

    picked = LETTERS.index(raw)
    if picked == question["answer"]:
        print("Correct!")
        return True
    right = question["choices"][question["answer"]]
    print(f"Wrong - the right answer was: {right}")
    return False


def grade(percent: float) -> str:
    """Return a friendly message for the final score."""
    if percent == 100:
        return "Perfect score! Outstanding."
    if percent >= 80:
        return "Great job!"
    if percent >= 50:
        return "Not bad - keep practicing."
    return "Keep learning, you will get there!"


def play_round() -> None:
    """Play one full round of shuffled questions."""
    questions = QUESTIONS[:]
    random.shuffle(questions)
    score = 0
    for i, question in enumerate(questions, start=1):
        if ask_question(question, i, len(questions)):
            score += 1

    percent = score / len(questions) * 100
    print("\n" + "=" * 40)
    print(f"Final score: {score}/{len(questions)} ({percent:.0f}%)")
    print(grade(percent))


def main() -> None:
    print("=" * 40)
    print("   Welcome to the Tech Quiz Game!")
    print("=" * 40)
    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        sys.exit(0)
