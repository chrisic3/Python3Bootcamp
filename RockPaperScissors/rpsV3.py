print("...Rock...")
print("...Paper...")
print("...Scissors...")

player1 = input("Player1, please make your move: ")
player2 = input("Player2, please make your move: ")

if player1 == player2:
    print("Draw!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player1 wins!")
    else:
        print("Something went wrong...")
elif player1 == "paper":
    if player2 == "rock":
        print("Player1 wins!")
    else:
        print("Something went wrong...")
elif player1 == "scissors":
    if player2 == "paper":
        print("Player1 wins!")
    else:
        print("Something went wrong...")
else:
    print("Player2 wins!")