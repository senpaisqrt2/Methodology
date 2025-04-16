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

    if ChosenGame == 'NOK':
        for n in range(0, 3):
            result = NOD.nok()
            if result['is_correct']:
                print('Correct!')
            else:
                print('Incorrect!')
                print('Your answer:', result['user_answer'])
                print(result['user_answer'], 'is wrong answer :( Correct answer is:', result['correct_answer'])
    elif ChosenGame == 'GeomProg':
        for n1 in range(0, 3):
            result = GeomProg.geomProg()
            if result['is_correct']:
                print('Correct!')
            else:
                print('Incorrect!')
                print('Your answer:', result['user_answer'])
                print(result['user_answer'], 'is wrong answer :( Correct answer is:', result['correct_answer'])

        print(f"Game over, {name}!")


if __name__ == '__main__':
    main()