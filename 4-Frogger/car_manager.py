from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
y_pos = [-200, -150, -100, -50, 0, 50, 100, 150, 200, 250]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.list_of_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        for i in range(0, len(self.list_of_cars)):
            self.list_of_cars[i].fd(self.speed)

    def car_maker(self):
        new_car_y_pos = random.choice(y_pos)

        if len(self.list_of_cars) >= 10:
            for car in self.list_of_cars[:20]:
                if car.pos()[0] < -300:
                    self.list_of_cars.remove(car)

            for car in self.list_of_cars[:8:-1]:
                if car.pos()[1] != new_car_y_pos:
                    self.new_car = Turtle(shape='square')
                    self.new_car.shapesize(1, 2), self.new_car.penup(), self.new_car.seth(-180)
                    self.new_car.color(random.choice(COLORS))
                    self.new_car.goto(320, new_car_y_pos)
                    self.list_of_cars.append(self.new_car)
                    return

        else:
            self.new_car = Turtle(shape='square')
            self.new_car.shapesize(1, 2), self.new_car.penup(), self.new_car.seth(-180)
            self.new_car.color(random.choice(COLORS))

            self.new_car.goto(320, new_car_y_pos)
            self.list_of_cars.append(self.new_car)

    def speed_increase(self):
        self.speed += MOVE_INCREMENT
