import prompt


def game(rules, qa_pairs):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rules)
    for (question, answer) in qa_pairs.items():
        print(f'Question: {question}')
        input_answer = prompt.string('Your answer: ')
        if input_answer == answer:
            print('Correct!')
        else:
            print(f'"{input_answer}" is wrong answer ;(. '
                  f'Correct answer was "{answer}".')
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def main():
    pass


if __name__ == '__main__':
    main()
