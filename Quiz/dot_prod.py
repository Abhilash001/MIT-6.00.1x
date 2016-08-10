def dotProduct(listA, listB):
	if listA == []:
		return 0
	else:
		return listA[0]*listB[0] + dotProduct(listA[1:], listB[1:])