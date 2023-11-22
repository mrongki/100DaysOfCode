from turtle import Turtle

COLOR = 'white'
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape='square')
        self.color(COLOR)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        self.sety(self.ycor() + 20)

    def move_down(self):
        self.sety(self.ycor() - 20)