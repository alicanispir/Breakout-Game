from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0,0)

    def move(self, x_direction, y_direction):
        if x_direction == "right":
            x_coordinate = self.xcor() + 2
        if x_direction == "left":
            x_coordinate = self.xcor() - 2
        if y_direction == "down":
            y_coordinate = self.ycor() - 2
        else:
            y_coordinate = self.ycor() + 2
        self.penup()
        self.goto(x_coordinate, y_coordinate)