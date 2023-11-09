import turtle

class Names(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def show_state(self, name, x, y):
        self.goto(x, y)
        self.write(arg=name, move=True, align="center")
