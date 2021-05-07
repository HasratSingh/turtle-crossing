import time
from turtle import Screen
from player import Player
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize Player, Cars and Scoreboard
player1 = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.update()


# Listener Function
def listener():
    player1.move_forward()
    screen.update()


# Initialize Listener
screen.listen()
screen.onkeypress(listener, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.add_car()
    car_manager.move_cars()
    # To find collision
    for car in car_manager.cars:
        if abs(car.xcor()-player1.xcor()) < 22 and abs(car.ycor()-player1.ycor()) < 28:
            game_is_on = False
            scoreboard.game_over()
            screen.onkeypress(fun=lambda: None, key="w")  # Removes event binding
    # When player reaches to top.
    if player1.finish():
        player1.reset_player()
        scoreboard.update_level()
        car_manager.move_distance += MOVE_INCREMENT
    screen.update()
screen.exitonclick()
