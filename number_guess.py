import random


def is_prime(n):  # has 2 factors
    fact = 0

    for i in range(1, n + 1):
        if n % i == 0:
            fact += 1

    if fact == 2:
        return True

    else:
        return False


# Game Starts Here

print("Welcome!")
lower = int(input("Enter The Lower Limit Of Range :- "))
upper = int(input("Enter The Upper Limit Of Range :- "))
print(f"Guess The Number Between {lower} To {upper}")

num_to_guess = random.randint(lower, upper)
num_of_guesses = 0
max_limit_of_guesses = 4  # Programmed For max limit Of 4 .

print(f"Number of Guesses Is {max_limit_of_guesses}")

while num_of_guesses != max_limit_of_guesses:
    choice = int(input("Enter Your Choice :- "))

    if choice == num_to_guess:
        print("You Win!")
        break

    elif choice != num_to_guess and num_of_guesses == 0:
        if is_prime(num_to_guess):
            print(f"HINT :- The Number To Guess Is Prime.")
        else:
            print(f"HINT :- The Number To Guess Is Not Prime.")

    elif choice != num_to_guess and num_of_guesses == 1:
        print(f"HINT :- The Number To Guess Is Between {num_to_guess - random.randint(1, 15)} To "
              f"{num_to_guess + random.randint(1, 15)} .")

    elif choice != num_to_guess and num_of_guesses == 2:
        if num_to_guess % 2 == 0:
            print("HINT :- The Number To Guess Is Even.")
        else:
            print("HINT :- The Number To Guess Is Odd.")

    else:
        print("You Lose!")
        print(f"The Number Was {num_to_guess}.")

    num_of_guesses += 1
