from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, posi):
        super(Paddle, self).__init__()
        self.posi = posi
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.posi)

    def up(self):
        y_axis = self.ycor() + 40
        self.goto(self.xcor(), y_axis)

    def backward(self):

        y_axis = self.ycor() - 20
        self.goto(self.xcor(), y_axis)


