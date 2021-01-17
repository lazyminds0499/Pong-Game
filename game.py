from turtle import Turtle, Screen
from score import Score
from paddle import Paddle
from ball import Ball
import time


class Game():
    def __init__(self):
        self.game_is_on = False
        self.l_score = Score((-100, 250))
        self.r_score = Score((100, 250))
        self.l_paddle = Paddle((-370, 0))
        self.r_paddle = Paddle((370, 0))
        self.screen = Screen()
        self.ball = Ball()
        self.setup_screen()

    def setup_screen(self):
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("MY Pong Game")
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkeypress(fun=self.r_paddle.up, key="Up")
        self.screen.onkeypress(fun=self.r_paddle.backward, key="Down")
        self.screen.onkeypress(fun=self.l_paddle.up, key="w")
        self.screen.onkeypress(fun=self.l_paddle.backward, key="s")
        # self.screen.exitonclick()

    def play(self):
        self.game_is_on = True
        while self.game_is_on:
            time.sleep(self.ball.move_speed)
            self.screen.update()
            self.ball.move()
            if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                self.ball.bounce_y()
            if self.ball.distance(self.r_paddle) < 50 and self.ball.xcor() > 320 or self.ball.distance(
                    self.l_paddle) < 50 and self.ball.xcor() < -320:
                self.ball.bounce_x()
            elif self.ball.xcor() > 380:
                self.l_score.score_count()
                self.ball.new_game()
            elif self.ball.xcor() < -380:
                self.r_score.score_count()
                self.ball.new_game()

    def stop(self):
        self.game_is_on = False

