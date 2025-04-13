import random

# print('Welcome to the Brain Games!')
# print('May I have your name?')
# name = input()
# print('Hello ' + name)
base_number = random.randint(2, 6)
progression_number = random.randint(2, 5)
blank_number = random.randint(1, 5)
updated_number = base_number
number_array = [base_number]
for i in range(9):
    number_array.append(updated_number*progression_number)
    updated_number = updated_number*progression_number
number_array[blank_number] = '..'
print('What number is missing in the progression?')
print(number_array)
userAnswer = int(input())
if userAnswer == base_number * progression_number ** blank_number:
    print('Correct!')
else:
    print('Incorrect!')
    print('Expected number:', base_number * progression_number ** blank_number)

