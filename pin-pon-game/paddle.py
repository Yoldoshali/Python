from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)

    def up(self):
        y_position = self.ycor() + 20
        self.goto(self.xcor(), y_position)

    def down(self):
        y_position = self.ycor() - 20
        self.goto(self.xcor(), y_position)


