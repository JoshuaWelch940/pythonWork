import random


while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

        if player == computer:
            print("computer: ",computer)
            print("player: ",player)
            print("tie!")

        elif player == "rock":
            if computer == "paper":
                print("computer: ",computer)
                print("player: ",player)
                print("lose!")
            if computer == "sissors":
                print("computer: ",computer)
                print("player: ",player)
                print("win!")
        elif player == "paper":
            if computer == "sissors":
                print("computer: ",computer)
                print("player: ",player)
                print("lose!")
            if computer == "rock":
                print("computer: ",computer)
                print("player: ",player)
                print("win!")
        elif player == "sissors":
            if computer == "rock":
                print("computer: ",computer)
                print("player: ",player)
                print("lose!")
            if computer == "papaer":
                print("computer: ",computer)
                print("player: ",player)
                print("win!")
    play_again = input("play agian? (yes/no): ").lower()

    if play_again != "yes":
        break
    
print("bye")