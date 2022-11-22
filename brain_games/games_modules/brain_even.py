from random import randrange
from ..game_engine import game


def main():
    max_num = 1000
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    question_answer_pairs = {}
    for _ in range(3):
        num = randrange(max_num)
        num_is_even = 'yes' if num % 2 == 0 else 'no'
        question_answer_pairs[num] = num_is_even
    game(rules, question_answer_pairs)


if __name__ == '__main__':
    main()
