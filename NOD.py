def nod(name):
    print('Find the smallest common multiple of given numbers.')
    n1 = 6
    n2 = 9
    n3 = 13
    print('Question:', n1, n2, n3)
    answer = int(input())
    if answer == n1 * n2 * n3:
        print('Your answer:', answer)
        print('Correct!')
    elif answer != n1 * n2 * n3:
        print('Your answer:', answer)
        print(answer, 'is wrong answer ;(. Correct answer was', n1 * n2 * n3)
        print('Let\'s try again, ' + name)
