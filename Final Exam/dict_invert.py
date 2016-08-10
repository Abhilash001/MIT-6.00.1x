from itertools import groupby
def dict_invert(d):
	return {k : sorted([i[0] for i in list(v)]) for k, v in groupby(d.items(),lambda x:x[1])}