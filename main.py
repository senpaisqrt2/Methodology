def main():
    import GeomProg
    import NOD

    print('Welcome to the Brain Games!\n')
    print('May I have your name?')

    name = input()

    print('Hello ' + name)
    print('\nWhat game do you wish to play?')
    print('Choose NOK or GeomProg')

    ChosenGame = input()

    # main.py (обновленная часть)
    if ChosenGame == 'NOK':
        for n in range(0, 3):
            result = NOD.nok()
            print(result['question'])
            answer = int(input())
            if answer == result['correct_answer']:
                print('Correct!')
            else:
                print('Incorrect!')
                print('Your answer:', answer)
                print(answer, 'is wrong answer :( Correct answer is:', result['correct_answer'])
    elif ChosenGame == 'GeomProg':
        for n1 in range(0, 3):
            result = GeomProg.geomProg()
            print(result['question'])
            answer = int(input())
            if answer == result['correct_answer']:
                print('Correct!')
            else:
                print('Incorrect!')
                print('Your answer:', answer)
                print(answer, 'is wrong answer :( Correct answer is:', result['correct_answer'])

        print(f"Game over, {name}!")


if __name__ == '__main__':
    main()