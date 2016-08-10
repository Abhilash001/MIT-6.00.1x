def flatten(aList):
	flat_list = []
	for an_object in aList:
		if type(an_object) is list:
			flat_list.extend(flatten(an_object))
		else:
			flat_list.append(an_object)
	return flat_list