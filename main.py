from turtle import *
from bullet import Bullet
from obstacles import Obstacles
from score_board import Points

player=Turtle()
screen=Screen()
screen.setup(width=800,height=750)
screen.listen()

score=Points()

obstacles_objects=[]

def setup():
    player.hideturtle()
    player.color("gold")
    player.pencolor("black")
    player.penup()
    player.speed(0)
    player.shape("turtle")
    player.turtlesize(3, 3,3)
    player.goto(x=0,y=-300)
    player.setheading(90)
    player.speed(6)
    player.showturtle()

def right():
    player.goto(player.xcor() + 51, player.ycor())

def left():
    player.goto(player.xcor() - 49, player.ycor())

def shoot():
    ball=Bullet(player.position())
    value=ball.moving(obstacles_objects)
    if value is not None:
        ball.delete_me()
        obstacles_objects[value].delete_me()
        obstacles_objects.pop(value)
        score.increment()
        ob = Obstacles()
        obstacles_objects.append(ob)

setup()

screen.onkey(right,"Right")
screen.onkey(left,"Left")
screen.onkey(shoot,"space")

for i in range(4):
    ob = Obstacles()
    obstacles_objects.append(ob)

done()