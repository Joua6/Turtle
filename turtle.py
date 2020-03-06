'''
Created on Feb 29, 2020

@author: ITAUser
'''
import turtle
t = turtle.Turtle()

t.pendown()
t.color('orange')
for i in range(4):
    t.forward(15)
    t.right(90)
t.penup()

t.goto(-120,130)
t.pendown()
t.color('red')
for i in range(3):
    t.forward(100)
    t.right(120)
t.penup())


