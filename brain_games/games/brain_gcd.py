from random import randrange
from ..game_engine import game


def gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


def main():
    MAX_NUM = 100
    rules = 'Find the greatest common divisor of given numbers.'
    question_answer_pairs = {}
    for _ in range(3):
        num1 = randrange(MAX_NUM)
        num2 = randrange(MAX_NUM)
        question = f'{num1} {num2}'
        answer = gcd(num1, num2)
        question_answer_pairs[question] = str(answer)
    game(rules, question_answer_pairs)


if __name__ == '__main__':
    main()
