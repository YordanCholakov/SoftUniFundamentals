number_of_strings = int(input())

for string in range(number_of_strings):
    word = input()
    if ',' not in word and '.' not in word and '_' not in word:
        print(f'{word} is pure.')
    else:
        print(f'{word} is not pure!')