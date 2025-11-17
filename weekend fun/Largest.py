number_one= int(input("Enter first integer: "))
number_two= int(input("Enter second integer: "))
number_three= int(input("Enter third integer: "))
largest= number_one
if number_two > largest:
	largest = number_two
if number_three > largest:
	largest=number_three
	print ('The largest number is ' , largest)

