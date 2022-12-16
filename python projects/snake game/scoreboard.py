from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score_board()
        self.hideturtle()

    def score_board(self):
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", False, align="center", font=("Arial", 15, "normal"))

    def score_total(self):
        self.score += 1
        self.clear()
        self.score_board()








