def main():
    import GeomProg
    import NOD

    print('Welcome to the Brain Games!')
    print('May I have your name?')

    name = input()

    print('Hello ' + name)
    print('What game do you wish to play?')
    print('Choose NOD or GeomProg')

    ChosenGame = input()

    if ChosenGame == 'NOD':
        NOD.nod(name)
    elif ChosenGame == 'GeomProg':
        GeomProg.geomProg()

if __name__ == '__main__':
    main()