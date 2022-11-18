from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# at the end of the project
# the snake class
# the food class
# the scoreboard class

# DETECT COLLISION WITH FOOD
# CREATE SCOREBOARD
# DETECT COLLISION WITH WALL
# DETECT COLLISION WITH TAIL

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# move snake forward
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    # detect the collision with food
    if snake.segments[0].distance(food) < 15:
        print("nom, nom, nom")
        snake.extend()
        food.refresh()
        scoreboard.hit()

    # detect collision with the wall

    if abs(snake.segments[0].xcor()) > 280 or abs(snake.segments[0].ycor()) > 280:
        scoreboard.game_over()
        game_is_on = False
        break

    # detect collision with the tail

    for x in range(1, (len(snake.segments)-1)):
        if snake.segments[0].distance(snake.segments[x]) < 10:
            scoreboard.game_over()
            game_is_on = False
            break


screen.exitonclick()
