from turtle import Turtle


class Score(Turtle):
    def __init__(self, posi):
        super(Score, self).__init__()
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(posi)
        self.score_count()

    def score_count(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score}", align="center", font=("courier", 20, "bold"))
        self.score += 1