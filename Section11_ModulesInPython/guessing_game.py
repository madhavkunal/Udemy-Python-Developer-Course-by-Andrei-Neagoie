import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Loop until the user guesses correctly
while True:
    try:
        guess = int(input("Please enter a number from 1-10: "))
        if 1 <= guess <= 10:
            if guess == random_number:
                print("You guessed correctly!")
                break  # Exit the loop if they guess right
            else:
                print("Please try again!")
        else:
            print("Please enter a number from 1-10.")
    except ValueError:
        print("Invalid input! Please enter a number.")
