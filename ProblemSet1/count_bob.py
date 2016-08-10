count = 0
for i in range(len(s)-2):
	str1=s[i:i+3]
	if str1=='bob':
		count+=1
print 'Number of times bob occurs is: '+str(count)