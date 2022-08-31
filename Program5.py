import random
min = 1
max = 6
roll_again = 'y'
while roll_again == 'Y':
    print('Rolling the Dice ....')
    val = random.randint(min,max)
    print(f'You got ....{val}')
    ro = input('Roll The Dice Again ? ....(Y/N)...')
    roll_again= ro.upper()