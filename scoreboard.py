from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(-20,260)
        self.color("white")

        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def hit(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.setposition(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

