import turtle
import random

#basic styling of the canvas
t = turtle.Turtle()
t.color("green")
t.pensize(2)
t.speed(100000000000000)
wn=turtle.Screen()
wn.bgcolor("grey")


#this function is for stopping the turtle to draw if it gets out of the screen
#wn is already defined inside turtle which acts as window and window_width and window_height will give actual value in numbers
#t is the point where turtle is, as default its the origin(0,0)
def isInScreen(wn, t):
	xmin = -wn.window_width()/2 
	xmax = wn.window_width()/2
	ymin = -wn.window_height()/2
	ymax = wn.window_height()/2

#	x = t.xcor()
#	y = t.ycor()
	x, y = t.pos()

	if x < xmin or x > xmax:
		return False
	if y < xmin or y > xmax:
		return False
	return True

# 0 = left and 1 = right
#randrange(4) means 0,1,2,3

while isInScreen(wn, t):
	t.fd(1)
	step = random.randrange(4)
	if step == 0:
		t.left(90)
	elif step == 1:
		t.right(90)
	elif step == 2:
		t.fd(0)
	else:
		t.bk(2)

turtle.mainloop()