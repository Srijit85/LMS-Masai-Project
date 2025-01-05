# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 02:08:07 2025

@author: Ateesh
"""

# Step 1: Define the Questions and Answers
def get_questions():
    return [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Rome", "D. Madrid"],
            "answer": "A"
        },
        {
            "question": "Which is the capital of Tamil Nadu?",
            "options": ["A. Delhi", "B. Chennai", "C. Mumbai", "D. dharavi"],
            "answer": "B"
        },
        {
            "question": "Where is Port Blair?",
            "options": ["A. Chennai", "B. Andaman Nicobar", "C. Assam", "D. Bengal"],
            "answer": "B"
        },
        {
            "question": "Where is the largest capital?",
            "options": ["A. America", "B. India", "C. japan", "D. China"],
            "answer": "D"
        },
        {
            "question": "Countries iwth multiple capitals?",
            "options": ["A. Sri Lanka", "B. Bolivia", "C. All of the above", "D. 8"],
            "answer": "C"
        }
    ]

# Step 2: Function to Display Questions and Get Answer
def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    
    # Get user's answer
    answer = input("Enter your answer (A, B, C, or D): ").upper()

    # Check if the answer is correct
    if answer == question_data["answer"]:
        return True
    return False

# Step 3: Main Quiz Game Function
def play_quiz():
    questions = get_questions()
    score = 0
    total_questions = len(questions)

    for i, question_data in enumerate(questions):
        print(f"\nQuestion {i + 1}:")
        correct = ask_question(question_data)
        if correct:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect.\n")

    # Step 4: Show Final Score
    print(f"Your final score is {score} out of {total_questions}.")

# Step 5: Start the Game
if __name__ == "__main__":
    print("Welcome to the Quiz Association of Capitals!")
    play_quiz()
