from random import randrange
from ..game_engine import game


def is_prime(num):
    div = 2
    while div * div <= num and num % div != 0:
        div += 1
    return 'yes' if div * div > num else 'no'


def main():
    max_num = 100
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question_answer_pairs = {}
    for _ in range(3):
        num = randrange(max_num)
        answer = is_prime(num)
        question = str(num)
        question_answer_pairs[question] = answer
    game(rules, question_answer_pairs)


if __name__ == '__main__':
    main()
