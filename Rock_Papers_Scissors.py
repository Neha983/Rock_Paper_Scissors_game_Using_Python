import random
def user_input():
    choice=input("Please Enter your Choice [ROCK, PAPER, SCISSORS]: ").upper()
    return choice
def computer_choice():
    input_data=["ROCK", "PAPER", "SCISSORS"]
    choice=random.choice(input_data)
    return choice
def determine_winner(user_data,computer_data):
    if user_data==computer_data:
        return "It's a Tie!"
    elif(user_data=="ROCK" and computer_data=="SCISSORS") or (user_data=="PAPER" and computer_data=="ROCK") or (user_data=="SCISSORS" and computer_data=="PAPER"):
       return "You Win!!"
    else:
        return "You Lose!!"
def Game_start():
    user_data=user_input()
    computer_data=computer_choice()
    print(f"\nYou choose {user_data}, computer choose {computer_data}.\n")
    winner=determine_winner(user_data,computer_data)
    print(winner)
Game_start()    
