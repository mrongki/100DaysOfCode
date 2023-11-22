from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 0
RIGHT = 180
COLOR = 'green'


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape('circle')
        self.head.shapesize(1.4, 1.4)

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)
        self.segments[-1].shape('tail')

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color(COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        self.segments[-1].shape('tail')
        self.segments[-2].shape('square')

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].pos()
            new_heading = self.segments[seg_num - 1].heading()
            self.segments[seg_num].goto(new_pos)
            self.segments[seg_num].setheading(new_heading)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape('circle')
        self.head.shapesize(1.4, 1.4)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    def right(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)
