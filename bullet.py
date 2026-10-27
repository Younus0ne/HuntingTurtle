import turtle

class Bullet(turtle.Turtle):
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.color("magenta")
        self.pencolor("black")
        self.penup()
        self.speed(0)
        self.shape("triangle")
        self.turtlesize(1, 1, 3)
        self.setheading(90)
        self.goto(position)
        self.showturtle()

    def moving(self,check_pos):
        for i in range(70):
            for j in check_pos:
                if self.distance(j.position()) < 40:
                    return check_pos.index(j)
                else:
                    self.forward(16)

    def delete_me(self):

        self.hideturtle()
        self.screen._turtles.remove(self)