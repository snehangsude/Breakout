from turtle import Turtle


class Bar:
    """
    Class object initializes the pad at the bottom to the screen.

    Methods:
        move_right(): Function to move the bar right on the x-axis
        move_let() : Function to move the bar left on the x-axis
    """

    def __init__(self):
        """Initializes the bar withe the shape, size, color and location"""
        self.bar = Turtle('square')
        self.bar.color('white')
        self.bar.penup()
        self.bar.goto(0, -250)
        self.bar.turtlesize(stretch_wid=0.6, stretch_len=3.2)

    def move_right(self):
        """Function to move the bar right on the x-axis"""
        if self.bar.xcor() < 205:
            self.bar.forward(28)

    def move_left(self):
        """Function to move the bar left on the x-axis"""
        if self.bar.xcor() > -205:
            self.bar.backward(28)
