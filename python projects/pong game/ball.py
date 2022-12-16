from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.x_move = 10
        self.y_move = 10
        self.speed_up = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_back(self):
        self.x_move *= -1
        self.speed_up *= 0.9


    def reset_position(self):
        self.goto(0, 0)
        self.bounce_back()


