from random import randrange


def rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(num):
    div = 2
    while div * div <= num and num % div != 0:
        div += 1
    return 'yes' if div * div > num else 'no'


def get_qa_pair():
    MAX_NUM = 100
    num = randrange(MAX_NUM)
    return str(num), is_prime(num)
