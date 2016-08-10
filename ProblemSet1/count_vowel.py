count = 0
for char in s:
    if char in 'aeiouAEIOU':
        count+=1
print 'Number of vowels: '+str(count)