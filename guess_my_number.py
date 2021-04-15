'''
This is my first python programme as a beginner
This program checks if a user's guess of a number matches that guessed by the computer
'''
print("WELCOME TO THE NUMBER GUESSING GAME")
print("-----------------------------------")
import random  # This imports the random module


def guess(x): #Defines a function called guess
    random_number = random.randint(1, 99)  # generates random numbers between 1 and 99 using the .randint function
    guess = 0  # Initializes the value of the variable guess to zero
    while guess != random_number:  # The While statement is used to execute a set of  if statements
        # as long as the guesssed number is not equal to the random numbers
        guess = int(input(f'Kindly guess a number between 1 and 99: '))  # This accepts input from the user
                                                                        # f' formats the string presented to the user
        if guess < random_number:
            print('Sorry,  Please guess again. Your guess is too low.')
        elif guess > random_number:
            print('Sorry, Please guess again. Your guess is too high.')

    print(f'Hurray. You have guessed the number {random_number} correctly')


guess(0)
