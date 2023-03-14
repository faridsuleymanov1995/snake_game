from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color('white')
        self.penup()
        self.hideturtle()
        self.increase()
    def increase(self):
        self.clear()
        self.score+=1
        self.goto(0, 270)
        self.write(f'score: {self.score} ', True, align='center', font=('arial', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER ', True, align='center', font=('arial', 20, 'normal'))
