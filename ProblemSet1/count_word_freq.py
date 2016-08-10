import re

def item_order(order):
	salad = 0
	hamburger = 0
	water = 0
	words = re.sub("[^\w]", " ",  order).split()
	for word in words:
		if word=='salad':
			salad+=1
		elif word=='hamburger':
			hamburger+=1
		elif word=='water':
			water+=1
	return ('salad:'+str(salad)+' hamburger:'+str(hamburger)+' water:'+str(water))