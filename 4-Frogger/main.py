import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.lv_board()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    car_manager.car_maker()
    car_manager.move()

    #Detect collision with car
    for car in car_manager.list_of_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful crossing
    if player.ycor()>300:
        player.start()
        car_manager.speed_increase()
        scoreboard.add_level()
        scoreboard.lv_board()


screen.exitonclick()
