# Yoda Spaceship using trinket
#by Tiffany Dicks on 9/16/2023

import turtle
import math

#background
screen = turtle.Screen()
screen.bgcolor("steelblue")

#create turtle
yoda = turtle.Turtle()
yoda.color("black")
yoda.shape("turtle")
yoda.speed(10)

#starting location
yoda.penup()
yoda.right(90)
yoda.forward(5)
yoda.pendown()
yoda.right(90)

# body of spaceship
def rectangle(width, length):
  yoda.fillcolor("white")
  yoda.begin_fill()
  yoda.forward(width)
  yoda.left(90)
  yoda.forward(length)
  yoda.left(90)
  yoda.forward(width)
  yoda.left(90)
  yoda.forward(length)
  yoda.left(90)
  yoda.end_fill()

print(rectangle(75, 150))

#tip of spaceship
def triangle(length):
  yoda.fillcolor("firebrick")
  yoda.begin_fill()
  yoda.right(60)
  yoda.forward(length)
  yoda.left(120)
  yoda.forward(length)
  yoda.end_fill()
  
print(triangle(75))

yoda.left(30)
yoda.forward(150)
  

#bottom fin of spaceship  
def bottom(width, length):
  yoda.fillcolor("firebrick")
  yoda.begin_fill()
  yoda.right(45)
  yoda.forward(length)
  yoda.left(135)
  yoda.forward(width)
  yoda.left(135)
  yoda.forward(length)
  yoda.end_fill()
  
print(bottom(132, 40))

#base of moon
yoda.penup()
yoda.right(45)
yoda.forward(240)
yoda.right(90)
yoda.forward(100)
yoda.pendown()
yoda.fillcolor("aliceblue")
yoda.begin_fill()
print(yoda.circle(50))
yoda.end_fill()

yoda.penup()
yoda.left(125)
yoda.forward(20)
yoda.pendown()
  
#moon craters  
def moon_circle(angle, length, size):
  yoda.penup()
  yoda.right(angle)
  yoda.forward(length)
  yoda.pendown()
  yoda.fillcolor("gainsboro")
  yoda.begin_fill()
  print(yoda.circle(size))
  yoda.end_fill()
moon_circle(90, 20, 7)
moon_circle(5, 40, 10)  
moon_circle(250, 50, 13)

yoda.color("black")
yoda.penup()
yoda.goto(-180, 100)
yoda.pendown()
yoda.write("3...2...1... Blast off!", None, None, "20pt bold")

yoda.speed(50)
yoda.penup()
yoda.goto(-40, -125)
yoda.left(-48)
