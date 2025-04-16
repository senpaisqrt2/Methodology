def nok():
    import random
    import math
    print('\nFind the smallest common multiple of given numbers.')
    n1 = random.randint(1, 15)
    n2 = random.randint(1, 15)
    n3 = random.randint(1, 15)
    print('Question:', n1, n2, n3)

    answer = int(input())

    expAnswer = math.lcm(n1, n2, n3)

    return {  # Возвращаем словарь
        'is_correct': answer == expAnswer,
        'user_answer': answer,
        'correct_answer': expAnswer
    }