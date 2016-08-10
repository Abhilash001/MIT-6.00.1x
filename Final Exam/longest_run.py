def longestRun(L):
	return [len(L[j:j+i]) for i in range(len(L),0,-1) for j in range(len(L)-i+1) if sorted(L[j:j+i]) == L[j:j+i]][0]