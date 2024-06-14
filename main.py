import random
import math

def guess_the_number():
    while True:
        # Taking Inputs
        lower = int(input("Enter Lower bound: "))

        # Taking Inputs
        upper = int(input("Enter Upper bound: "))

        # generating random number between the lower and upper
        x = random.randint(lower, upper)
        print("\n\tYou've only", 
              round(math.log(upper - lower + 1, 2)),
              "chances to guess the integer!\n")

        # Initializing the number of guesses.
        count = 0

        # for calculation of minimum number of guesses depends upon range
        max_guesses = round(math.log(upper - lower + 1, 2))

        while count < max_guesses:
            count += 1

            # taking guessing number as input
            guess = int(input("Guess a number: "))

              # Condition testing
            if x == guess:
                if count == 1:
                    print("Congratulations you did it in", count, "try")
                else:  
                    print("Congratulations you did it in", count, "tries")
                # Once guessed, loop will break
                break
            elif x > guess:
                print("You guessed too small!")
            elif x < guess:
                print("You guessed too high!")

        # If Guessing is more than required guesses and the player didn't guess correctly, shows this output.
        if x != guess:
            print("\nThe number is %d" % x)
            print("\tBetter Luck Next time!")

        # Asking the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

# Call the function to start the game
guess_the_number()
