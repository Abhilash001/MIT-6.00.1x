import math

fixedPay=round(balance/120)*10
temp=balance
while balance>0.0 :
	fixedPay+=10
	balance=temp
	for month in range(12) :
		balance-=fixedPay
		balance=round(balance+annualInterestRate/12.0*balance,2)
print ("Lowest Payment: "+str(fixedPay))