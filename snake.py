from turtle import Turtle



class Snake():
    def __init__(self):
        self.snake_d = []
        self.create_snake()
        self.head = self.snake_d[0]
        self.a = 3

    def create_snake(self):
        x = 0
        for i in range(0, 3):
            snake = Turtle('square')
            snake.color('white')
            snake.penup()
            snake.goto(x, 0)
            self.snake_d.append(snake)
            x -= 20
    def bigger(self):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(self.snake_d[-1].position())
        self.snake_d.append(snake)

    def move(self):
        for i in range(len(self.snake_d) - 1, 0, -1):
            new = self.snake_d[i - 1].position()
            self.snake_d[i].goto(new)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
         self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)