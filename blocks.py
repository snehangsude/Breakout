from turtle import Turtle

COLOR = ["tomato", "tomato1", "tomato2", "tomato3", "tomato4"]


class Blocks:
    """
    Class object initializes the blocks on the top of the screen.

    Methods:
        generate_blocks(): Function to generate the blocks and then append them into a single list of blocks
    """

    def __init__(self):
        """Initializes the list to append the blocks"""
        self.all_blocks = []

    def generate_blocks(self):
        """
        Function to generate the blocks and then append them into a single list of blocks
        Changes the x-coordinate every iterations
        Changes the y-coordinate every 10 iterations
        """
        y = 230
        for rows in range(5):
            x = -230
            for _ in range(10):
                block = Turtle('square')
                block.color(COLOR[rows])
                block.penup()
                block.goto(x, y)
                block.turtlesize(stretch_len=2, stretch_wid=1)
                self.all_blocks.append(block)
                x += 50
            y -= 30
