from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        car = Turtle()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(1, 2)
        car.penup()
        car.goto(300, random.randint(-250, 250))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(new_x, car.ycor())

    def increase_step(self):
        self.car_speed += MOVE_INCREMENT

