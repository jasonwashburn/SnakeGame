from turtle import Turtle
STARTING_POSITION = (0, 0)
STARTING_LENGTH = 3
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        self.segments = [Turtle(shape='square') for _ in range(STARTING_LENGTH)]
        for num, piece in enumerate(self.segments):
            piece.color('white')
            piece.penup()
            piece.setx(STARTING_POSITION[0] - (num * 20))

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Note the position of the segment in front of the current piece,
            # then move the current piece to that position
            prev_seg_loc = (self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
            self.segments[seg_num].goto(prev_seg_loc)

        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
