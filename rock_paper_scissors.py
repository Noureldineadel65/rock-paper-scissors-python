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
choices = ["rock", "paper", "scissors"]
drawn_choices = [rock, paper, scissors]
num_user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
num_computer_choice = random.randint(0, 2)
user_choice = choices[num_user_choice]
computer_choice = choices[num_computer_choice]
state = "You lose!"
if user_choice == computer_choice:
    state = "It's a Tie."
else:
    if user_choice == "rock" and computer_choice == "scissors":
        state = "You WIN!"
    elif user_choice == "paper" and computer_choice == "rock":
        state = "You WIN!"
    elif user_choice == "scissors" and computer_choice == "paper":
        state = "You WIN!"

print(drawn_choices[num_user_choice])
print("Computer chose:")
print(drawn_choices[num_computer_choice])
print(state)
