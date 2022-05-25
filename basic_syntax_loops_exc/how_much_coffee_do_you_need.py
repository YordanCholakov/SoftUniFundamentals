number_of_coffees = 0
command = ''

while True:
    command = input()
    if command ==  'END' and number_of_coffees <= 5:
        print(number_of_coffees)
        break
    elif command == 'END' and number_of_coffees > 5:
        print('You need extra sleep')
        break
    if command == 'coding' or command == 'movie' or command == 'dog' or command == 'cat':
        number_of_coffees+=1
    if command == 'CODING' or command == 'MOVIE' or command == 'DOG' or command == 'CAT':
        number_of_coffees+=2
