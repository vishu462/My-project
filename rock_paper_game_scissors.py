import random

option = ["rock", "paper", "scissors"]

userInput = str(input("enter your choice (rock, paper, scissors): ")).lower()

if userInput not in option:
    print("You have entered wrong input")
else:

    computer_choice = random.choice(option)
    if userInput == "rock":
        if computer_choice == "paper":

            print(f"computer choice: {computer_choice} \nYou win")
        else:
            print(f"computer choice: {computer_choice} \nYou lose")
    elif userInput == "paper":
        if computer_choice == "rock":
            print(f"computer choice: {computer_choice} \nYou win")
        else:
            print(f"computer choice: {computer_choice} \nYou lose")
    elif userInput == "scissors":
        if computer_choice == "paper":
            print(f"computer choice: {computer_choice} \nYou win")
        else:
            print(f"computer choice: {computer_choice} \nYou lose")
