import random
from turtle import Turtle

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []

    def increment_speed(self):
        self.move_distance += MOVE_INCREMENT

    def generate_new_car(self):
        car = Turtle()
        car.shape("square")
        car.setheading(180)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

        car.penup()
        car.goto(280, random.randint(-200, 200))

        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() > -300:
                car.forward(self.move_distance)
            else:
                car.reset()
                car.hideturtle()
                self.cars.remove(car)

    def detect_collision_with_turtle(self, turtle_pos):
        for car in self.cars:
            if car.distance(turtle_pos) < 30:
                return True

        return False
