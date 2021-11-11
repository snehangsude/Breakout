import time
from turtle import Screen
from bar import Bar
from blocks import Blocks
from ball import Ball

screen = Screen()
screen.bgcolor("grey20")  # Setting background color
screen.title("Breakout Game")  # Setting the title of the screen
screen.setup(width=520, height=600)  # Setting the height and width of the screen
screen.tracer(0)  # Turning the animation off

# Pad
bar = Bar()

# Blocks
blocks = Blocks()
blocks.generate_blocks()

# Ball
ball = Ball()

screen.listen()  # Initializes keyboard responses
screen.onkey(bar.move_right, "Right")
screen.onkey(bar.move_left, "Left")

while True:
    screen.update()  # Turning animation on
    time.sleep(0.08)
    ball.move()

    # Co-ordinates to bounce from the bar
    if -225 > ball.ball.ycor() > -240 and ball.ball.distance(bar.bar.pos()) < 38:
        ball.bounce_bar()

    # Co-ordinates to bounce from the ceiling
    if ball.ball.ycor() > 270:
        ball.bounce_ceil()

    # Co-ordinates to bounce from the walls
    if (ball.ball.xcor() > 230 or ball.ball.xcor() < -230) and ball.ball.ycor() > -255:
        ball.bounce_walls()

    # Distance to bounce from the blocks
    for i in blocks.all_blocks:
        if ball.ball.distance(i.pos()) < 33:
            ball.bounce_blocks()
            i.goto(10000, -1000)

    # Restart the game if the ball misses the bar
    if ball.ball.ycor() < -300:
        ball.restart()
