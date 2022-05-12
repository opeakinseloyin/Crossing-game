# Importing the Turtle class in order to create Score class using the inheritance method
from turtle import Turtle


class Score(Turtle):
    """ This class creates objects that writes the score on the screen and manages the score of the player"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-230, 260)

    def writing(self):
        """ This function writes the score on the screen"""
        self.clear()
        self.write(arg=f"level: {self.score + 1}", align="center", font=("Courier", 14, "normal"))

    def level_up(self):
        """ This function increases the score"""
        self.score += 1

    def game_over(self):
        """ This function writes game over on the screen"""
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Courier", 18, "normal"))
