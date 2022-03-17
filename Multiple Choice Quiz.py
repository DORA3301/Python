# Multiple Choice Quiz Using Python

from Question import Question

question_prompts = [
    "What is the color of the sky?\n(a) Red\n(b) Blue\n(c) Green\n\nEnter your answer: ",
    "\nWhat is the color of a lemon?\n(a) Red\n(b) Blue\n(c) Yellow\n\nEnter your answer: ",
    "\nWhat is the color of an apple?\n(a) Red\n(b) Blue\n(c) Magenta\n\nEnter your answer: ",
    "\nWhat is 2 x 4?\n(a) 8\n(b) 7\n(c) 6\n\nEnter your answer: ",
    "\nHow many days are in March?\n(a) 30\n(b) 31\n(c) 29\n\nEnter your answer: "
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")


run_test(questions)

