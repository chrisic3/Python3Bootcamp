from random import random

rand_num = randint(0, 2)

print("...Rock...")
print("...Paper...")
print("...Scissors...")

player = input("Player1, please make your move: ").lower()

if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"Computer plays {computer}")

if player == computer:
    print("Draw!")
elif player == "rock":
    if computer == "scissors":
        print("Player wins!")
    elif computer == "paper":
        print("Computer wins!")
    else:
        print("Something went wrong...")
elif player == "paper":
    if computer == "rock":
        print("Player wins!")
    elif computer == "scissors":
        print("Computer wins!")
    else:
        print("Something went wrong...")
elif player == "scissors":
    if computer == "paper":
        print("Player wins!")
    elif computer == "rock":
        print("Computer wins!")
    else:
        print("Something went wrong...")
else:
    print("Something went wrong...")