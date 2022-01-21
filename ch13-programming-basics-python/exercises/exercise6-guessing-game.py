import random

"""
Write a program that:

runs until the user guesses a number (hint: while loop)
generates a random number between 1 and 9 (including 1 and 9)
asks the user to guess the number
then prints a message to the user, whether they guessed too low, too high
if the user guesses the number right, print out YOU WON! and exit the program
Hint: Use the built-in random module to generate random numbers
"""


def play_guessing_game():
    random_number = random.randrange(1, 10, 2)
    prompt = "Welcome to the Guessing Game! I'm thinking of a number between 1 and 9 (inclusive).\n"
    prompt += "Can you guess what it is?\n"
    game_over = False

    while game_over == False:
        guess = input(prompt)
        if guess == 'exit':
            break
        try:
            guess_as_int = int(guess)
            if guess_as_int > 9 or guess_as_int < 1:
                raise ValueError
                
            print(f"Your guess: {guess_as_int}")
            if guess_as_int == random_number:
                print("YOU WON!")
                game_over = True
            elif guess_as_int > random_number:
                print("Too High!")
            else:
                print("Too Low!")
        except ValueError:
            print("Please enter an integer between 1 and 9 inclusive.")

    print("Exiting game...")


play_guessing_game()



