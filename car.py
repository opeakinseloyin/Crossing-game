# Importing the randint function and the Turtle class in order to create the Car class
from turtle import Turtle
from random import randint


class Car:
    """ This class creates object that act like cars. Moving across the screen"""
    def __init__(self):
        self.car_list = []

    def create_car(self):
        """ This function creates the car"""
        # Using the if statement and randint function
        # in oder to reduce the amounts of cars being created at a giving time
        if randint(1, 3) == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            # Using the randint function to create a random color scheme
            car.color(randint(0, 250), randint(0, 250), randint(0, 250))
            car.penup()
            car.setheading(180)
            # Using the randint function to create the car in a random y position
            car.goto(300, randint(-230, 230))
            self.car_list.append(car)

    def move(self):
        """ This function moves the car across the screen"""
        for car in self.car_list:
            car.forward(10)
