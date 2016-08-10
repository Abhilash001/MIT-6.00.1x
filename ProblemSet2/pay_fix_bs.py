import math

low=balance/12
high=(balance*(1+annualInterestRate/12.0)**12)/12.0
temp=balance
while low<=high :
	fixedPay=(low+high)/2.0
	balance=temp
	for month in range(12) :
		balance-=fixedPay
		balance=round(balance+annualInterestRate/12.0*balance,2)
	if abs(balance-0.0)<=0.01 :
		break
	elif balance>0.0 :
		low=fixedPay
	elif balance<0.0 :
		high=fixedPay
print ("Lowest Payment: "+str(round(fixedPay,2)))