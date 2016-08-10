def isPalindrome(aString):
	aString=aString.lower()
	for index in range(len(aString)/2):
		if aString[index] is not aString[len(aString)-index-1]:
			return False
	return True