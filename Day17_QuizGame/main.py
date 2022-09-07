"""
Day 17 - Coffee Machine (OOP)

This program aims to simulate a Quiz Game.
"""
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


def create_question_bank():
    question_bank = []
    for question in question_data:
        question_bank.append(Question(question["text"], question["answer"])) 
    return question_bank


if __name__ == "__main__":
    question_bank = create_question_bank()
    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("Congratulations! You've completed the quiz.")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
