total_bill= float(input("Enter Total Bill: "))
membership= input("Are you a member? ")
if total_bill > 1000 or total_bill == 1000 and (membership == 'yes'):
	print('10% off')
elif total_bill > 1000 or total_bill == 1000 and (membership == 'no'):
	print('5% off')
else:
	print ('Pay full bill of ', total_bill, ' no discount') 