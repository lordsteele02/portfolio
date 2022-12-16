from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
UP = 90
down = 270
game_is_on = True


screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.tracer(0)

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

net = Turtle()
net.speed("fastest")
net.setposition(0, 300)
net.color("white")
net.hideturtle()
net.setheading(270)

for _ in range(30):
    net.pendown()
    net.forward(10)
    net.penup()
    net.forward(10)


while game_is_on:
    time.sleep(ball.speed_up)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_back()
        ball.speed_up -= 0.01

    if ball.xcor() > 380:
        print("ball out of bounds")
        ball.reset_position()
        scoreboard.l_point()
        ball.speed_up = 0.1

    if ball.xcor() < -380:
        print("ball out of bounds")
        ball.reset_position()
        scoreboard.r_point()
        ball.speed_up = 0.1

screen.exitonclick()
