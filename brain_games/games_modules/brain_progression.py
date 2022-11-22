from random import randrange
from ..game_engine import game


def main():
    progression_max_start = 100
    max_step = 10
    rules = 'What number is missing in the progression?'
    question_answer_pairs = {}
    for _ in range(3):
        num = randrange(progression_max_start)
        step = randrange(max_step)
        progression = []
        for _ in range(10):
            progression.append(str(num))
            num += step
        index = randrange(10)
        answer = progression[index]
        progression[index] = '..'
        question = ' '.join(progression)
        question_answer_pairs[question] = answer
    game(rules, question_answer_pairs)


if __name__ == '__main__':
    main()
