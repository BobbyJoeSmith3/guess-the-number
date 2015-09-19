# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0, 100)
    print "the secret number is", secret_number


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game

    # remove this when you add your code
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game

    pass

def input_guess(guess):
    # convert user input to interger
    user_input = int(guess)

    # main game logic goes here

    print "Guess was", user_input


# create frame
frame = simplegui.create_frame('Guess The Number', 300, 300)


# register event handlers for control elements and start frame

# input field for player guesses
inp = frame.add_input('Enter Guess', input_guess, 100)

frame.start()

# call new_game
new_game()


# always remember to check your completed program against the grading rubric
