# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# initialize global variables used in your code
num_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, num_of_guesses
    secret_number = random.randrange(0, num_range)
    print "New game. Range is 0 to", num_range
    # determine number of guesses to start with
    if num_range == 100:
        num_of_guesses = 7
    elif num_range == 1000:
        num_of_guesses = 10
    # tell player how many guesses they have left
    print "Number of remaining guesses is", num_of_guesses
    # create space between entries
    print ""
    # decrement the number of guesses player has left
    num_of_guesses = num_of_guesses - 1

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range, num_of_guesses
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range, num_of_guesses
    num_range = 1000
    new_game()

def input_guess(guess):
    global num_of_guesses
    # convert user input to interger
    user_input = int(guess)
    # print user's guess to console and number of guesses left
    print "Guess was", user_input
    print "Number of remaining guesses is", num_of_guesses
    # main game logic goes here
    if num_of_guesses == 0:
        print "You ran out of guesses. The number was", secret_number
        print ""
        new_game()
    elif secret_number > user_input:
        print "Higher"
    elif secret_number < user_input:
        print "Lower"
    elif secret_number == user_input:
        print "Correct"
        print ""
        new_game()
    # decrement the number of guesses player has left
    num_of_guesses = num_of_guesses - 1
    # create space between entries
    print ""

# create frame
frame = simplegui.create_frame('Guess The Number', 300, 300)

# register event handlers for control elements and start frame
# new game buttons
zero_to_one_hundred = frame.add_button('Range is [0,100)', range100, 150)
zero_to_one_thousand = frame.add_button('Range is [0,1000)', range1000, 150)
# input field for player guesses
inp = frame.add_input('Enter Guess', input_guess, 150)


# call new_game
new_game()

# start all frame event handlers
frame.start()

# always remember to check your completed program against the grading rubric
