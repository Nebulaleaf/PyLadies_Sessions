pc_choice = 'rock'
user_choice = input('rock, paper, or scissors?')

if user_choice == 'rock':
    if pc_choice == 'rock':
        print('Draw.')
    elif pc_choice == 'scissors':
        print ('You win!')
    elif pc_choice == 'paper':
        print ('Computer won!')
elif user_choice == 'scissors':
    if pc_choice == 'rock':
        print('Computer won!')
    elif pc_choice == 'scissors':
        print('Draw.')
    elif pc_choice == 'paper':
        print('You win!')
elif user_choice == 'paper':
    if pc_choice == 'rock':
        print('You win!')
    elif pc_choice == 'scissors':
        print('Computer won!')
    elif pc_choice == 'paper':
        print('Draw.')
else:
    print('I do not understand.')