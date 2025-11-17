number_one= float(input("Enter first integer: "))
number_two= float(input("Enter second integer: "))
if number_one > 0 and number_two > 0:
	print('Q1')
if number_one < 0 and number_two > 0:
	print('Q2')
if number_one < 0 and number_two < 0:
	print('Q3')
if number_one > 0 and number_two < 0:
	print('Q1')
if number_one == 0 and number_two == 0:
	print('Origin')	
if number_one != 0 and number_two == 0:
	print('X-axis')
if number_one == 0 and number_two != 0:
	print('Y-axis')