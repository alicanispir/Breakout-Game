from turtle import Turtle

class Block(Turtle):
    def __init__(self, x_loc, y_loc, color, length):
        super().__init__()
        #self.paddle.hideturtle()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=4, stretch_len=length)
        self.penup()
        self.goto(x_loc, y_loc)