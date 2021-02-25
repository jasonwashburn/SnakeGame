from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 275)

        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)