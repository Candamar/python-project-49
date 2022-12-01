from random import randrange


def rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_qa_pair():
    MAX_NUM = 1000
    num = randrange(MAX_NUM)
    num_is_even = 'yes' if num % 2 == 0 else 'no'
    return str(num), num_is_even
