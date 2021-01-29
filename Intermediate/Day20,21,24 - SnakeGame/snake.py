from turtle import Turtle, Screen
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.add_initial_segments()
        self.head = self.segments[0]

    def add_initial_segments(self):
        for i in range(0, 3):
            self.add_segment(position=(-20 * i, 0))

    def add_segment(self, position):
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)

        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def turn_up(self):
        self.segments[0].setheading(90)

    def turn_down(self):
        self.segments[0].setheading(270)

    def turn_right(self):
        self.segments[0].setheading(0)

    def turn_left(self):
        self.segments[0].setheading(180)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.add_initial_segments()
        self.head = self.segments[0]
