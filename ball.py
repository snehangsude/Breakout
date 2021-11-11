from turtle import Turtle
from random import choice
from operator import add, sub

SYMBOLS = {'+': add,
           '-': sub,
           }


class Ball:
    """
    Class object initializes the ball at the center to the screen.

    Methods:
        move(): Initializes the movement of the ball towards the 3rd or the 4th quadrant
        bounce_bar(): Changes the y-axis if the ball hits the pad
        bounce_walls(): Changes the x-axis if the ball hits any walls
        bounce_ceil(): Changes the y-axis if the ball hits the top ceil/border
        bounce_blocks(): Changes the y-axis if the ball hits any of the blocks
        restart(): Resets the location of the ball and selects a quadrant once out of play
    """

    def __init__(self):
        """Initializes the ball on the screen setting the size, color, shape"""
        self.ball = Turtle('circle')
        self.ball.penup()
        self.ball.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.ball.color('DarkGoldenrod2')
        self.sign = choice(list(SYMBOLS.keys()))
        self.x = 10
        self.y = 10

    def move(self):
        """Initializes the movement of the ball towards the 3rd or the 4th quadrant"""
        new_x = SYMBOLS.get(self.sign)(self.ball.xcor(), self.x)
        new_y = self.ball.ycor() - self.y
        self.ball.goto(new_x, new_y)

    def bounce_bar(self):
        """Changes the y-axis if the ball hits the pad"""
        self.y *= -1

    def bounce_walls(self):
        """Changes the x-axis if the ball hits any walls"""
        self.x *= -1

    def bounce_ceil(self):
        """Changes the y-axis if the ball hits the top ceil/border"""
        self.y *= -1

    def bounce_blocks(self):
        """Changes the y-axis if the ball hits any of the blocks"""
        self.y *= -1

    def restart(self):
        """Resets the location of the ball and selects a quadrant once out of play"""
        self.ball.home()
        self.move()
