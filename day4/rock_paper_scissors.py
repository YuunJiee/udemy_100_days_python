import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choose_list = [Rock, Paper, Scissors]
user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choose = random.randint(0, 2)


if(user_choose > 2 or user_choose < 0):
    print("You typed an invalid number. You lose!")
else:
    print("Your choose:")
    print(choose_list[user_choose])

    print("Computer's choose:")
    print(choose_list[computer_choose])

    if(user_choose == computer_choose):
        print("Tie")
    elif(user_choose - computer_choose) % 3 == 1:
        print("You Win!")
    else:
        print("You lose...")
