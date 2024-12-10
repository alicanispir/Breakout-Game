from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_loc, y_loc):
        super().__init__()
        #self.paddle.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=20)
        self.penup()
        self.goto(x_loc, y_loc)
        #self.paddle.showturtle()

    def go_right(self):
        if self.xcor() < 740:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())
        else:
            new_x = self.xcor() + 0
            self.goto(new_x, self.ycor())

    def go_left(self):
        if self.xcor() > -760:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())
        else:
            new_x = self.xcor() - 0
            self.goto(new_x, self.ycor())