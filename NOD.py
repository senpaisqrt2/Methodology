def nok(name):
    import random
    import math
    print('\nFind the smallest common multiple of given numbers.')
    n1 = random.randint(1, 15)
    n2 = random.randint(1, 15)
    n3 = random.randint(1, 15)
    print('Question:', n1, n2, n3)

    answer = int(input())

    expAnswer = math.lcm(n1, n2, n3)

    if answer == expAnswer:
        print('Your answer:', answer)
        print('Correct!')

    elif answer != expAnswer:
        print('Your answer:', answer)
        print(answer, 'is wrong answer ;( Correct answer was', expAnswer)
        print('Let\'s try again, ' + name)