from random import randrange


def gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


def rules():
    print('Find the greatest common divisor of given numbers.')


def get_qa_pair():
    MAX_NUM = 100
    num1 = randrange(MAX_NUM)
    num2 = randrange(MAX_NUM)
    question = f'{num1} {num2}'
    answer = gcd(num1, num2)
    return question, str(answer)
