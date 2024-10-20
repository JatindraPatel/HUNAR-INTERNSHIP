import random
import time
questions = [
    ("What is the output of the following code:\n```python\nprint(2 + 3 * 4)\n```", "14"),
    ("Which data type is used to represent a sequence of characters in Python?", "string"),
    ("What is the purpose of the `break` statement in a loop?", "to exit the loop prematurely"),
    ("How do you define a function in Python?", "def function_name():"),
    ("What is the result of the expression `5 // 2`?", "2"),
    ("Which of the following is a valid variable name in Python?", "my_variable"),
    ("What is the output of the following code:\n```python\nprint(5 % 2)\n```", "1"),
    ("Which keyword is used to define a class in Python?", "class"),
    ("What is the purpose of the `len()` function?", "to find the length of a sequence")
]

def quiz():
    score = 0
    random.shuffle(questions)  

    print("Welcome to the Quiz!")

    for question, answer in questions:
        print(" ")
        print(question)
        print("Time remaining :- ", 30)  

        start_time = time.time()
        user_answer = input("Your answer :-  ")
        end_time = time.time()

        time_taken = end_time - start_time

        if time_taken > 30:
            print("Time's up! The correct answer is :- ", answer, "\n")
        elif user_answer.lower() == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect Answer ." )
            print("The correct answer is :- ", answer, "\n")

        print("Your Current score :- ", score, "/", len(questions), "\n")

    print("Quiz completed !")
    print("Your final score is :-", score, "/", len(questions))

    if score >= len(questions) / 2:
        print("Congratulations ! You passed the quiz.")
    else:
        print(" Better luck next time. Keep practicing !")

quiz()