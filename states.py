from turtle import Turtle


class States(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.hideturtle()

    def write_on_map(self, state, map_x, map_y):
        self.goto(map_x, map_y)
        self.write(f"{state}", False, align="center", font=("Arial", 12, 'normal'))
