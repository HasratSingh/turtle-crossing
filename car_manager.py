from turtle import Turtle
from random import choice, randint, choices

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    cars = []

    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.add_car()

    def add_car(self):
        if choices(population=[True, False], weights=[1, 5], k=1)[0]:  # To restrict no of cars added.
            car = Turtle("square")
            car.color(choice(COLORS))
            car.penup()
            car.seth(180)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(320, randint(-260, 260))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)
