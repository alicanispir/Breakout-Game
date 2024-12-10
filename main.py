from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import Block
from score import Score
import time
import random

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")

global pad1, ball, score, game_is_on
pad1 = Paddle(0, -500)

score = Score()

def create_blocks():
    global blue_blocks
    a = -860
    blue_blocks = []
    while a < 900:
        random_length = random.randint(3,8)
        col = a
        block = Block(col, 200 - 0 * 60, color="blue", length=random_length)
        a = a + 20 + random_length * 20
        blue_blocks.append(block)
    a = -860
    while a < 900:
        random_length = random.randint(3,8)
        col = a
        block = Block(col, 200 - 2 * 60, color="red", length=random_length)
        a = a + 20 + random_length * 20
        blue_blocks.append(block)

    a = -860
    while a < 900:
        random_length = random.randint(3,8)
        col = a
        block = Block(col, 200 + 2 * 60, color="yellow", length=random_length)
        a = a + 20 + random_length * 20
        blue_blocks.append(block)

    a = -860
    while a < 900:
        random_length = random.randint(3,8)
        col = a
        block = Block(col, 200 + 4 * 60, color="green", length=random_length)
        a = a + 20 + random_length * 20
        blue_blocks.append(block)

ball = Ball()
y_dir = "up"
x_dir = "right"

time_ball = 0.0001
game_is_on = True

def game():
    global game_is_on, x_dir, y_dir, ball, pad1, score, blue_blocks
    create_blocks()
    while game_is_on:
        screen.update()
        screen.listen()
        time.sleep(time_ball)
        screen.onkey(pad1.go_right, "Right")
        screen.onkey(pad1.go_left, "Left")

        ball.move(x_dir, y_dir)

        if ball.ycor() == 500:
            y_dir = "down"


        if ball.xcor() == 920:
            x_dir = "left"
        elif ball.xcor() == -940:
            x_dir = "right"

        x_distance = abs(pad1.xcor() - ball.xcor())

        if x_distance < 200 and -505 < ball.ycor() < -490 and x_dir == "right":
            print("cancanali")
            x_dir = "right"
            y_dir = "up"
        elif x_distance < 200 and -505 < ball.ycor() < -490 and x_dir == "left":
            print("alicancan")
            x_dir = "left"
            y_dir = "up"

        for brick in blue_blocks:
            if ball.distance(brick) < 70 and x_dir == "right" and y_dir == "up":
                x_dir = "right"
                y_dir = "down"
                brick.hideturtle()
                blue_blocks.remove(brick)
                score.player_point()
                break
            elif ball.distance(brick) < 70 and x_dir == "left" and y_dir == "up":
                x_dir = "left"
                y_dir = "down"
                brick.hideturtle()
                blue_blocks.remove(brick)
                score.player_point()
                break
            elif ball.distance(brick) < 70 and x_dir == "right" and y_dir == "down":
                x_dir = "right"
                y_dir = "up"
                brick.hideturtle()
                blue_blocks.remove(brick)
                score.player_point()
                break
            elif ball.distance(brick) < 70 and x_dir == "left" and y_dir == "down":
                x_dir = "left"
                y_dir = "up"
                brick.hideturtle()
                blue_blocks.remove(brick)
                score.player_point()
                break

        if ball.ycor() == -520:
            score.game_over()
            game_is_on = False

        if len(blue_blocks) == 0:
            screen.update()
            score.player_win()
            game_is_on = False
def restart_game():
    global game_is_on, pad1, ball, score, blue_blocks
    ball.goto(0, 0)
    game_is_on = True
    y_dir = "up"
    x_dir = "right"
    score.player_score = 0
    score.updatescoreboard()
    a = len(blue_blocks)
    print(blue_blocks)
    for block in blue_blocks[:]:  # Iterate over a shallow copy of the list
        block.hideturtle()
        blue_blocks.remove(block)  # Safe to remove the element from the original list
        print(len(blue_blocks))
    screen.update()
    screen.listen()
    game()
screen.onkey(restart_game, "r")
game()
screen.exitonclick()