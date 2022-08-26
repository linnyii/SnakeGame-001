from turtle import Turtle

# we do not put below default value into class Snake
# Since we might change those default value
# then we can change directly from here without touching class Snake
from typing import List, Any

starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position)

    def move(self):
        len_segments = len(self.segments)
        for seg_num in range(len_segments - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def go_up(self):
        if self.head.heading() != down:
            self.head.heading(up)

    def go_down(self):
        if self.head.heading() != up:
            self.head.heading(down)

    def go_left(self):
        if self.head.heading() != right:
            self.head.heading(left)

    def go_right(self):
        if self.head.heading() != left:
            self.head.heading(right)
