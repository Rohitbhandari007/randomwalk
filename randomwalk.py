import random

def random_walk(n):
	#return coordinates after 'n' block random walk
	x,y = 0,0
	for i in range(n):
		step = random.choice(['N','S','E','W'])
		if step == 'N':
			y = y + 1
		elif step == 'S':
			y = y - 1
		elif step == 'E':
			x = x + 1
		elif:
			x = x - 1

	return(x, y)

