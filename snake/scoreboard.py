from turtle import Turtle

ALIGNMENT = 'center'
V_ALIGNMENT = 274
FONT = ('Courier', 18, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, V_ALIGNMENT)
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}\tHigh Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as writefile:
                writefile.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.show_score()
