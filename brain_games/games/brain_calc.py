from random import randrange
from random import choice


def rules():
    print('What is the result of the expression?')


def get_qa_pair():
    MAX_NUM = 100
    operators = ("+", "-", "*")
    num1 = randrange(MAX_NUM)
    num2 = randrange(MAX_NUM)
    operator = choice(operators)
    question = f'{str(num1)} {operator} {str(num2)}'
    answer = (num1 + num2 if operator == '+' else
              num1 - num2 if operator == '-' else
              num1 * num2)
    return question, str(answer)
