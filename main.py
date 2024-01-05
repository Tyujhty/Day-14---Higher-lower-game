import random
from replit import clear
from art import logo, vs
from game_data import data

def random_choice(data):
    return random.choice(data)
    
def user_choice():
    return input("Who has more followers?: Type 'A' or 'B' ").upper()

def compare(choice_a, choice_b, user_answer):
    result_vs = ''
    if choice_a['follower_count'] > choice_b['follower_count']:
        result_vs = choice_a
    else: 
        result_vs = choice_b
        
    print(result_vs)

def game():
    print(logo)
    print("Who has the more followers? Try to guess and defeate the computer\n")

    choice_a = random_choice(data)
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
    print(vs)
    choice_b = random_choice(data)
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")

    user_answer = user_choice()
    print(user_answer)
    compare(choice_a, choice_b, user_answer)
game()