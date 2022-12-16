from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.position = x_pos
        self.speed("fastest")
        self.penup()
        self.setposition(self.position)
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.setheading(90)

    def up(self):
        self.forward(20)

    def down(self):
        self.back(20)
