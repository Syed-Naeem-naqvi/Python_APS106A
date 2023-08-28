# APS106 Lab 1 - Drawing Shapes with Turtle
# Student Name: Naeem
# PRA Section: 0104


################################################
# Part 2 - Draw your initials
################################################

# provide access to the Turtle module
import turtle

# bring the turtle to life and call it alex
alex = turtle.Turtle()


# use alex to draw your first and last initials
# TODO: WRITE YOUR CODE HERE

r = 50
theta = 153.43

alex.up()
alex.goto(-r, r)
alex.setheading(90)
alex.down()
alex.circle(r, 270)
alex.circle(-r, 270)
alex.up()
alex.goto(0, -2*r)

alex.down()
alex.forward(4*r)
alex.right(theta)
alex.forward(2*(5**(1/2))*r)
alex.left(theta)
alex.forward(4*r)

turtle.done()


