"""Use while True for unlimited guesses; 
    use for loop for limited attempts."""

import random     # It is used to generate pseudo-random numbers for various distributions like, Games(Dice roll, guessing)

# Generate a random number between 1 and 100
a = random.randint(1,100)        # randint() is used to generate a random integer between 2 specified values
guesses = 1
n = 0

# Keep looping until the user guesses the correct number
while(a != n):
    
    n = int(input("Guess the number :"))
    if(a>n):
        print("Higher number please...")
        guesses += 1

    elif(a<n):
        print("Lower number please...")
        guesses += 1

print(f"You have guessed the correct number {n} in {guesses} attempts.")
