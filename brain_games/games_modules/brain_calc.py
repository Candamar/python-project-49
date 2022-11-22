from random import randrange
from random import choice
from ..game_engine import game


def main():
    max_num = 100
    rules = 'What is the result of the expression?'
    operators = ('+', '-', '*')
    question_answer_pairs = {}
    for _ in range(3):
        num1 = randrange(max_num)
        num2 = randrange(max_num)
        operator = choice(operators)
        question = f'{str(num1)} {operator} {str(num2)}'
        answer = (num1 + num2 if operator == '+' else
                  num1 - num2 if operator == '-' else
                  num1 * num2)
        question_answer_pairs[question] = str(answer)
    game(rules, question_answer_pairs)


if __name__ == '__main__':
    main()
