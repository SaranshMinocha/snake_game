from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake game ')
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

def restart_game():
    global restart_snake
    snake.restart()
    scoreboard.reset_score()
    screen.onkey(None, "r")
    restart_snake=False

game_is_on=True
restart_snake=False

while game_is_on:
    screen.update()
    time.sleep(0.2)
    if not restart_snake:
        snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        restart_snake=True
        if restart_snake:
            scoreboard.game_over()
            screen.onkey(restart_game,"r")

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            restart_snake = True
            if restart_snake:
                scoreboard.game_over()
                screen.onkey(restart_game, "r")



screen.exitonclick()