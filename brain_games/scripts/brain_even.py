#! /usr/bin/env python


import prompt
from random import randrange


def main():
    max_num = 1000
    correct_answer_count = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while correct_answer_count >= 0 and correct_answer_count < 3:
        num = randrange(max_num)
        num_is_even = 'yes' if num % 2 == 0 else 'no'
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if answer == num_is_even:
            correct_answer_count += 1
            print('Correct!')
        else:
            correct_answer_count = -1
            print(f'"{answer}" is wrong answer ;(. \
Correct answer was "{num_is_even}".')
    if correct_answer_count == 3:
        print(f'Congragulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
