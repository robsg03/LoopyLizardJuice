#Rock Paper Scissors Game Module 3 - Feb 7, 2026

import random

user_action = input("Enter Rock, Paper, or Scissors: ")
possible_action = ['rock', 'paper', 'scissors']
cpu_action = random.choice(possible_action)
print('You chose ' + user_action + '. Computer chose ' + cpu_action)

if user_action.lower() == cpu_action:
    print("Draw. Try again.")
elif user_action.lower == 'rock':
    if cpu_action == 'scissors':
        print("Rock Smashes scissors. You Win!")
    else:
        print('Paper covers rock. You lose!')

elif user_action.lower() == 'scissors':
    if cpu_action == 'paper':
        print("Scissors shreds paper. You Win!")
    else:
        print('Rock smashes scissors. You lose!')

elif user_action.lower() == 'paper':
    if cpu_action == 'rock':
        print("Paper covers rock. You Win!")
    else:
        print('Scissors shreds paper. You lose!')