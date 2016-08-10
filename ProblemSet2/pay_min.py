import math

Total_pay=0.0
for month in range(12) :
	print ("Month: "+str(month+1))
	minMonthPay=round(balance*monthlyPaymentRate,2)
	print ("Minimum monthly payment: "+str(minMonthPay))
	Total_pay+=minMonthPay
	balance-=minMonthPay
	balance=round(balance+annualInterestRate/12.0*balance,2)
	print ("Remaining balance: "+str(balance))
print ("Total paid: "+str(Total_pay))
print ("Remaining balance: "+str(balance))