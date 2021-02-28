from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, "normal")


def load_high_score():
    with open('data.txt') as file:
        contents = file.read()
        if contents == '':
            return 0
        else:
            return int(contents)


def new_high_score(score):
    with open("data.txt", mode='w') as file:
        file.write(str(score))


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 275)
        self.score = 0
        self.high_score = load_high_score()
        load_high_score()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            new_high_score(self.high_score)
        self.score = 0
        self.update_score()
