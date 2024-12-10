from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.updatescoreboard()

    def updatescoreboard(self):
        self.clear()
        self.goto(0, 500)
        self.write(f"Score: {self.player_score}", align="center", font=("Courier", 80, "normal"))

    def player_point(self):
        self.player_score += 1
        self.updatescoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 500)
        self.write("Game Over! Press on 'r' to restart.", align="center", font=("Courier", 50, "normal"))

    def player_win(self):
        self.clear()
        self.goto(0, 500)
        self.write("You won! Press on 'r' to restart.", align="center", font=("Courier", 50, "normal"))