import random

random_num = random.randint(0, 10)
it_took = 0
number_guess = 5


def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("This is not a number please try again.")
            continue
        else:
            return userInput
            break


# This line is for testing the game, it can be removed once it is presented to users.
print(random_num)
print("Welcome to the guessing game, you will have 5 guesses to guess a number.")
guess = inputNumber("Please enter a number from 0 and 10: ")

while number_guess > 1:

    if guess > random_num:
        it_took += 1
        number_guess -= 1
        guess = int(input("Too high, try again: "))
    elif guess < random_num:
        it_took += 1
        number_guess -= 1
        guess = int(input("Too Low, try again: "))
    elif guess == random_num:
        it_took += 1
        number_guess -= 1
        break

if number_guess <= 1:
    print("I am sorry, you have run out of guesses.")
else:
    print("Winner, Winner, Chicken Dinner")
    print("Congratulations it took you %s guesses to guess the magic number." % it_took)
