from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.penup()
        self.color("green")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1  # this is to change y direction when it bounces
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def new_game(self):
        # y_axis = random.randint(-220, 220)
        self.goto(x=0, y=0)
        self.bounce_x()
        self.move_speed = 0.1

