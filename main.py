import random
from replit import clear
from art import logo, vs
from game_data import data


def user_choice():
    return input("Who has more followers?: Type 'A' or 'B' ").upper()

def compare(computer_choices, score):
    print(f"Compare A: {computer_choices[0]['name']}, a {computer_choices[0]['description']}, from {computer_choices[0]['country']}")
    print(vs)
    print(f"Against B: {computer_choices[1]['name']}, a {computer_choices[1]['description']}, from {computer_choices[1]['country']}\n")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if computer_choices[0]['follower_count'] > computer_choices[1]['follower_count']:
        result = 'A'
        computer_choices[1] = random.choice(data)
    else:
        result = 'B'
        computer_choices[0] = computer_choices[1]
        computer_choices[1] = random.choice(data)

    if user_guess == result:
        score += 1
        print(f"\nYou're right! Current score: {score}")
        return True, score
    else:
        clear()
        print(f"Sorry, you didn't guess. Your final score: {score}")
        return False, score
    
def game():
    keep_playing = True
    print(logo)
    print("Who has the more followers? Try to guess and defeate the computer\n")
    
    computer_choices = []
    '''Computer make a dictionary with 2 results'''
    for _ in range(2):
        computer_choices.append(random.choice(data))
    score = 0
    while keep_playing:
        keep_playing, score = compare(computer_choices, score)
game()