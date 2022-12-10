from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.X = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.X} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def reset(self):
        if self.X > self.high_score:
            self.high_score = self.X
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.X = 0
        self.clear()
        self.write(f"Score: {self.X} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def increase(self):
        self.X += 1
