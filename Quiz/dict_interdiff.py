def dict_interdiff(d1, d2):
	intersect = {key: f(d1[key], d2[key]) for key in d1.keys() if key in d2.keys()}
	difference = {key: d1[key] for key in d1.keys() if key not in d2.keys()}
	difference.update({key: d2[key] for key in d2.keys() if key not in d1.keys()})
	return (intersect, difference)