from turtle import Turtle

Alignment = "center"
Font = ("Ariel", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    # use turtle to write somethin
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=Alignment, font=Font)

    def increase_score(self):
        self.score += 1
        self.clear()  # clear what turtle wrote before
        self.update_score()  # call this function and let turtle write something

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=Alignment, font=Font)