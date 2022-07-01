import random


def dice_roller():
    return random.randint(1, 6)


while True:
    print(dice_roller())
    print("Do You Want To Roll The Dice Again ?")
    choice = input("[y/n]  :-")
    if choice == 'y':
        continue

    elif choice == 'n':
        break

    else:
        print("Wrong Choice Entered!")
        break
