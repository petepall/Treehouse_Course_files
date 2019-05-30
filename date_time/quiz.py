from questions import Add, Multiply
from typing import Tuple, Union
import datetime
import random


class Quiz:
    questions: list = []
    answers: list = []

    def __init__(self):
        question_types: tuple = (Add, Multiply)
        # generate 10 random questions with numbers from 1 to 10
        for _ in range(10):
            num1: int = random.randint(1, 10)
            num2: int = random.randint(1, 10)
            question: tuple = random.choice(question_types)(num1, num2)
            self.questions.append(question)

    def take_quiz(self) -> str:
        self.start_time = datetime.datetime.now()

        for question in self.questions:
            self.answers.append(self.ask(question))
        else:
            self.end_time = datetime.datetime.now()
        return self.summary()

    def ask(self,
            question: Union[Add, Multiply]
            ) -> Tuple[bool, datetime.timedelta]:
        correct = False
        question_start = datetime.datetime.now()
        answer = input(question.text + ' = ')
        # check the answer
        if answer == str(question.answer):
            correct = True

        question_end = datetime.datetime.now()
        return correct, question_end - question_start

    def total_correct(self) -> int:
        # return the total # of correct answers
        total: int = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        # print how many you got right and the total # of questions. 5/10
        print(f"You got {self.total_correct()} out of "
              f"{len(self.questions)} right")

        # print the total time for the quiz: 30 seconds!
        print(f"It took you {(self.end_time - self.start_time).seconds} "
              f"seconds total.")


Quiz().take_quiz()
