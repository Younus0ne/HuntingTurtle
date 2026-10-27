import turtle,random

class Obstacles(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        colors = ["red", "green", "blue", "orange", "purple", "pink", "black", "brown", "darkred",
                  "darkgreen", "navy", "violet", "turquoise", "salmon", "khaki", "tomato"]
        self.hideturtle()
        self.color(random.choice(colors))
        self.penup()
        self.speed(0)
        self.shape("square")
        self.turtlesize(1, 3, 17)
        self.goto(x=random.randint(-345, 345), y=random.randint(20, 300))
        self.showturtle()

    def delete_me(self):
        self.hideturtle()
        self.screen._turtles.remove(self)
