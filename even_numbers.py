numbers = int(input())

for i in range(1, numbers+1):
    current_number = int(input())
    if current_number % 2 != 0:
        print(f'{current_number} is odd!')
        break
else:
    print(f'All numbers are even.')