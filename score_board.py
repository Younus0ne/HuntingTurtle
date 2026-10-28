import turtle

class Points(turtle.Turtle):
    points = 0
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,320)
        self.draw_score()

    def increment(self):
        Points.points+=1
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.write(arg=f"Points : {Points.points}", align="center", font=("Arial", 30, "bold"))

