import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess it right.")

secret_number = random.randint(1, 100)
guess_count = 0

while guess_count < 5:
    guess = int(input("Guess the number: "))
    guess_count += 1
    
    if guess < secret_number:
        print("Too low. Guess again.")
    elif guess > secret_number:
        print("Too high. Guess again.")
    else:
        print(f"Congratulations! You guessed it right in {guess_count} tries.")
        break

if guess_count == 5:
    print(f"Sorry, you couldn't guess the number. The number was {secret_number}.")

