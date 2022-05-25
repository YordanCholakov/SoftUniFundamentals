number_of_messages = int(input())
for i in range(1, number_of_messages+1):
    current_code = int(input())
    if current_code == 88:
        print(f'Hello')
    elif current_code == 86:
        print(f'How are you?')
    elif current_code !=88 and current_code!=86 and current_code < 88:
        print(f'GREAT!')
    else:
        print('Bye.')