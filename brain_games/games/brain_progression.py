from random import randrange


def rules():
    print('What number is missing in the progression?')


def get_qa_pair():
    PROGRESSION_MAX_START = 100
    MAX_STEP = 10
    num = randrange(PROGRESSION_MAX_START)
    step = randrange(MAX_STEP)
    progression = []
    for _ in range(10):
        progression.append(str(num))
        num += step
    index = randrange(10)
    answer = progression[index]
    progression[index] = '..'
    return ' '.join(progression), answer
