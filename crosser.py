# Importing the Turtle class in order to create Crosser class using the inheritance method
from turtle import Turtle


class Crosser(Turtle):
    """ This class creates objects that the player uses to cross the road"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def move(self):
        """ This function moves the crosser 20 paces"""
        self.forward(20)

    def refresh(self):
        """ This function moves the crosser back to the starting point"""
        self.goto(0, -280)
