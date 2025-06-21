import random

emojis = {'p':'📃', 'r': '🪨', 's': '✂️'}
choices = (tuple(emojis.keys()))

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

def get_user_input():
    user_input = (input("Rock, Paper,or Scissors? (r/p/s)"))
    while True:
        if user_input not in choices:
            print ('Invalid choice!')
        else:
            print(f'You chose: {emojis[user_input]}')
            return user_input

def computer_choice():
    return random.choice (choices)

def give_feedback(user, computer):
    while True:
        if user == computer:
            return "Tie!"
        elif (user == PAPER and computer == ROCK) or \
            (user == SCISSORS and computer == PAPER) or \
            (user == ROCK and computer == SCISSORS):
            return "You Win!"
        else:
            return "You lose!"
        break

def rock_paper_scissors():
    print('Welcome to rock, paper, scissors!')
    while True:
        user_input = get_user_input()
        computer_input = computer_choice()
        print(f'Computer chose: {emojis[computer_input]}')
        result = give_feedback(user_input, computer_input)
        print(result)
        play_again = input("Do you want to play again? (y/n:) ")
        if play_again != 'y':
            print('Thanks for playing! Goodbye.')
            break
                    
rock_paper_scissors()