import prompt


def main(game):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    game.rules()
    for _ in range(3):
        question, answer = game.get_qa_pair()
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
