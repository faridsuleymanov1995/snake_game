from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen1 = Screen()
screen1.tracer(0)
screen1.setup(width=600,height=600)
screen1.bgcolor('black')

snake1 = Snake()
food1 = Food()
score = ScoreBoard()
screen1.listen()
screen1.onkey(snake1.up,key='Up')
screen1.onkey(snake1.down,key='Down')
screen1.onkey(snake1.left,key='Left')
screen1.onkey(snake1.right,key='Right')


end = True
speed = 0.15
y = 5
while end:
    screen1.update()
    time.sleep(speed)
    snake1.move()
    # increase speed of snake
    if len(snake1.snake_d)  == y:
        speed -= 0.005
        y += 5
    # detect collision with food and make snake bigger
    if snake1.head.distance(food1) < 16:
        food1.refresh()
        score.increase()
        snake1.bigger()
    # detect collision with wall
    if not -270 < snake1.head.position()[0] < 270 or  not -270 < snake1.head.position()[1] < 270:
        score.game_over()
        end = False
    # detect collision with tail
    for i in snake1.snake_d[1:]:
        if snake1.head.distance(i) < 10:
            score.game_over()
            end = False

screen1.exitonclick()
