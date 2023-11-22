from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-275, -275)
        self.pendown()
        self.color('white')
        self.goto(275, -275)
        self.goto(275, 275)
        self.goto(-275, 275)
        self.goto(-275, -275)
