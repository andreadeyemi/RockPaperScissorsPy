import random
import os
import re

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_play_status():
    valid_responses = ['yes', 'no']
    while True:
        try:
            response = input('Do you wish to play again? (Yes or No): ')
            if response.lower() not in valid_responses:
                raise ValueError('Yes or No only')

            if response.lower() == 'yes':
                return True
            else:
                clear_screen()
                print('Thanks for playing!')
                exit()

        except ValueError as err:
            print(err)

def display_choice(choice):
    ascii_art = {
        'R': '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
        'P': '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
        'S': '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    }

    print(ascii_art[choice])

def play_rps():
    play = True
    while play:
        clear_screen()
        print('')
        print('Rock, Paper, Scissors - Shoot!')

        user_choice = input('Choose your weapon [R]ock, [P]aper, or [S]cissors: ')

        if not re.match("[SsRrPp]", user_choice):
            print('Please choose a letter:')
            print('[R]ock, [P]aper, or [S]cissors')
            continue

        user_choice = user_choice.upper()
        print('You chose:')
        display_choice(user_choice)

        choices = ['R', 'P', 'S']
        opp_choice = random.choice(choices)

        print('I chose:')
        display_choice(opp_choice)

        if opp_choice == user_choice:
            print('Tie!')
        elif (opp_choice == 'R' and user_choice == 'S') or \
             (opp_choice == 'S' and user_choice == 'P') or \
             (opp_choice == 'P' and user_choice == 'R'):
            print('I win!')
        else:
            print('You win!')

        play = check_play_status()

if __name__ == '__main__':
    play_rps()
