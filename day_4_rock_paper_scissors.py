"""Day 3 - Rock, Paper, Scissors"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

option_dict = {
    1: rock,
    2: paper,
    3: scissors
}

ai_option = random.randint(1, 3)

player_option = int(input("Enter:\n'1' for Rock\n'2' for Paper\n'3' for Scissors\n"))


def calculate_result(ai_chose, player_chose):
    if player_chose == ai_chose:
        return "It's a draw!"
    elif player_chose == 1 and ai_chose == 3:
        return "You win!"
    elif ai_chose == 1 and player_chose == 3:
        return "You lose"
    elif ai_chose > player_chose:
        return "You lose"
    elif player_chose > ai_chose:
        return "You win!"



if player_option in option_dict:
    print(f"You chose: {option_dict[player_option]}")
    print(f"The AI chose: {option_dict[ai_option]}")
    print(f"The result is: {calculate_result(ai_option, player_option)}")

else:
    print("You typed an invalid number, you lose!")

