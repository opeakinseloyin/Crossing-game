# Importing the sleep function, Car, Score, Screen and Crosser class in order to create the turtle crossing program
from car import Car
from time import sleep
from score import Score
from turtle import Screen
from crosser import Crosser

# Creating a screen object from the Screen class and setting its height and width to 600
screen = Screen()
screen.setup(600, 600)
# Using the tracer function to stop lag and using the colormode function to change the color mode
# in order to create random colors for each car
screen.tracer(0)
screen.colormode(255)
# Setting the title of the screen
screen.title("Ope's Turtle Crossing Game")

# Creating the crosser, car and score objects from their respective classes
timmy = Crosser()
car = Car()
score = Score()

# Using the listen function to allow the screen to take key input to do certain functions and defining them below
screen.listen()
screen.onkey(timmy.move, "Up")
# Defining the variable game on to stay True whenever the game is being played and turn False when game is over
game_on = True

# Using the while loop to loop over the game parameters so as to keep the game running
while game_on:
    # Works in hand with the tracer function
    screen.update()
    # Used to slow down the program for a certain amount of seconds
    sleep(0.1)
    # Writing the score on the top of the screen
    score.writing()
    # Creating a car
    car.create_car()
    # Making the car created move
    car.move()

    # Using the for loop to loop through the cars created and move them by 20 paces
    for cars in car.car_list:
        # Using the if statement to check if there is a collision between the car and the crosser
        if cars.distance(timmy) < 22:
            # Creating the loosing condition
            game_on = False
            # Writing game over on the screen when the game comes to an end
            score.game_over()

    # Using the if statement to check if the crosser has safely made it to the other side
    if timmy.ycor() > 290:
        # Adding a point when the crosser crosses the road
        score.level_up()
        # Taking the crosser back to starting point to start over again
        timmy.refresh()

# Using the exitonclick function to keep the screen up until the game has ended
screen.exitonclick()


