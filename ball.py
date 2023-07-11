from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("slow")
        self.shape("circle")
        self.color("white")
        self.numx = 5
        self.numy = 5
        self.ball_speed = 0.002

    def move(self ):
        new_x = self.xcor() + self.numx
        new_y = self.ycor() + self.numy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.numy *= -1

    def bounce_x(self):
        self.numx *= -1
        self.ball_speed *= 0.99

    def restart(self):
        self.goto(0, 0)
        self.numx *= -1
        self.ball_speed = 0.002



