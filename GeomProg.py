def geomProg():
    import random
    base_number = random.randint(2, 6)
    progression_number = random.randint(2, 5)
    blank_number = random.randint(1, 5)
    updated_number = base_number
    number_array = [base_number]
    for i in range(9):
        number_array.append(updated_number * progression_number)
        updated_number *= progression_number
    number_array[blank_number] = '..'
    print('What number is missing in the progression?')
    print(number_array)
    answer = int(input())
    expAnswer = base_number * progression_number ** blank_number
    return {  # Возвращаем словарь
        'is_correct': answer == expAnswer,
        'user_answer': answer,
        'correct_answer': expAnswer
    }