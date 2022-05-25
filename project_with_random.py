import random
print('Welcome to the final days of Sofia Open 2022!')
print('Enter your semi-finalist: ')
semifinalist_1 = input()
semifinalist_2 = input()
semifinalist_3 = input()
semifinalist_4 = input()
finalist_1 = ''
finalist_2 = ''
sf1 = ''
sf2 = ''

print(f'{semifinalist_1}, {semifinalist_2}, {semifinalist_3} and {semifinalist_4} are your semi-finalists!')

sf_options = ["1vs2","1vs3", "1vs4","2vs3", "3vs4", "2vs4" ]
draw = random.choice(sf_options)
print(f'Here is the draw!')
if draw == '1vs2':
    print(f'{semifinalist_1} vs. {semifinalist_2}')
    print(f'{semifinalist_3} vs. {semifinalist_4}')
elif draw == '1vs3':
    print(f'{semifinalist_1} vs. {semifinalist_3}')
    print(f'{semifinalist_2} vs. {semifinalist_4}')
elif draw == '1vs4':
    print(f'{semifinalist_1} vs. {semifinalist_4}')
    print(f'{semifinalist_2} vs. {semifinalist_3}')
elif draw == '2vs3':
    print(f'{semifinalist_2} vs. {semifinalist_3}')
    print(f'{semifinalist_1} vs. {semifinalist_4}')
elif draw == '2vs4':
    print(f'{semifinalist_2} vs. {semifinalist_4}')
    print(f'{semifinalist_1} vs. {semifinalist_3}')
elif draw =='3vs4':
    print(f'{semifinalist_3} vs. {semifinalist_4}')
    print(f'{semifinalist_1} vs. {semifinalist_2}')

possible_results = ['6:0','6:1','6:2','6:3','6:4','7:5','7:6','0:6','1:6','2:6','3:6','4:6','5:7','6:7']

print('If you want to see the results, type PLAY: ')
action = input()
if action == 'PLAY':
