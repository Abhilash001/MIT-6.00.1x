def satisfiesF(L):
	L[:] = [s for s in L if f(s) is True]
	return len(L)
run_satisfiesF(L, satisfiesF)