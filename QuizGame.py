import random


def display_question(question):
    print(question['question'])
    for i, choice in enumerate(question['choices'], 1):
        print(f"{i}. {choice}")


def welcome():
    print("Welcome to the Quiz Game!")
    print("Rules: \n 1. You'll be asked 3 multiple-choice questions. \n 2. Each question is of 1 marks. \n Let's see "
          "how well you know")


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect.")
            print(f"The correct answer is: {correct_answer}")

    def play(self):
        welcome()
        start = input("Press S to start the quiz: ")
        if start == "s":
            random.shuffle(self.questions)
            for question in self.questions:
                display_question(question)
                user_answer = input("Your answer: ")
                self.evaluate_answer(user_answer, question['answer'])
            print("Thankyou for attending the quiz")
            print(f"Your final score is: {self.score}/{len(self.questions)}")


quiz_questions = [
    {
        "question": "Which language is easy to learn?",
        "choices": ["Java", "Python", "C", "C++"],
        "answer": "2"
    },
    {
        "question": "Is Python is Case Sensitive?",
        "choices": ["Yes", "No"],
        "answer": "1"
    },
    {
        "question": "What is the output of the % operator?",
        "choices": ["Quotient", "Division", "Remainder", "None of the above"],
        "answer": "3"
    }
]

if __name__ == "__main__":
    game = Quiz(quiz_questions)
    game.play()
