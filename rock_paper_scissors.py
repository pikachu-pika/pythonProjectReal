import random

lis = ["ROCK", "PAPER", "SCISSOR"]

print("Welcome!", "\n")
while True:
    computer = random.choice(lis)
    print("ROCK / PAPER / SCISSOR   |  R/P/S  |  r/p/s")
    choice = input("Enter :-")

    print(f"Computer : {computer}")

    if choice in ["ROCK", "R", "r"]:
        print(f"You : ROCK")
        if computer == "ROCK":
            print("TIE!")
        elif computer == "PAPER":
            print("YOU LOSE!")
        elif computer == "SCISSOR":
            print("YOU WIN!")

    elif choice in ["PAPER", "P", "p"]:
        print(f"You : PAPER")
        if computer == "ROCK":
            print("YOU WIN!")
        elif computer == "PAPER":
            print("TIE!")
        elif computer == "SCISSOR":
            print("YOU LOSE!")

    elif choice in ["SCISSOR", "S", "s"]:
        print(f"You : SCISSOR")
        if computer == "ROCK":
            print("YOU LOSE!")
        elif computer == "PAPER":
            print("YOU WIN!")
        elif computer == "SCISSOR":
            print("TIE!")

    else:
        print("WRONG CHOICE ENTERED")

    print("DO YOU WANT TO PLAY AGAIN")
    choice = input("[Y/N | y/n] :-")
    if choice in ['Y', "y"]:
        continue

    elif choice in ['N' ,"n"]:
        break

    else:
        print("WRONG CHOICE ENTERED!")
        break

print("THANK YOU FOR PLAYING!")
