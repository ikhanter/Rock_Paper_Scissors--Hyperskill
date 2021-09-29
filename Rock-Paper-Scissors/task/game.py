import random
import sys


default_option = ['paper', 'scissors', 'rock']
print('Enter your name: ', end='')
username = input()
print(f'Hello, {username}')
option_input = input()
if option_input == '':
    options = default_option
else:
    options = [s for s in option_input.split(',')]
print('Okay, let\'s start')
with open('rating.txt', 'r') as rating_file:
    for line in rating_file:
        record_user, record_score = line.split()
        if username == record_user:
            current_score = int(record_score)
            break
        else:
            current_score = 0

while True:
    user_choice = input()
    if user_choice in options:
        comp_choice = random.choice(options)
        while options.index(user_choice) != len(options) // 2:
            if options.index(user_choice) > len(options) // 2:
                options.append(options.pop(0))
            elif options.index(user_choice) < len(options) // 2:
                options.insert(0, options.pop(-1))
        if comp_choice == user_choice:
            current_score += 50
            print(f'There is a draw {user_choice}')
            # draw_counter += 1
        elif (options.index(user_choice) - options.index(comp_choice)) < 0:
            print(f'Sorry, but the computer chose {comp_choice}')
            current_score = current_score
            # lose_counter += 1
        elif (options.index(user_choice) - options.index(comp_choice)) > 0:
            current_score += 100
            print(f'Well done. The computer chose {comp_choice} and failed')
            # win_counter += 1
    elif user_choice == '!rating':
        print(f'Your rating: {current_score}')
    elif user_choice == '!exit':
        # print(f'Win: {win_counter}\tDraw: {draw_counter}\tLose: {lose_counter}')
        print('Bye!')
        sys.exit()
    else:
        print('Invalid input')