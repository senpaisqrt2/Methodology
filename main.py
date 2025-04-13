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
            NOD.nok(name)
    elif ChosenGame == 'GeomProg':
        for n1 in range(0, 3):
            GeomProg.geomProg()

if __name__ == '__main__':
    main()