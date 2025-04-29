def nok():
    import random
    import math
    n1 = random.randint(1, 15)
    n2 = random.randint(1, 15)
    n3 = random.randint(1, 15)
    question = 'Find the smallest common multiple of given numbers.\nQuestion: ' + f"{n1} {n2} {n3}"
    expAnswer = math.lcm(n1, n2, n3)
    return {
        'question': question,
        'correct_answer': expAnswer
    }

    expAnswer = math.lcm(n1, n2, n3)

    return {  # Возвращаем словарь
        'is_correct': answer == expAnswer,
        'user_answer': answer,
        'correct_answer': expAnswer
    }