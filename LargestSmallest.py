number_one= int(input("Enter first integer: "))
number_two= int(input("Enter second integer: "))
number_three= int(input("Enter third integer: "))
sum_of_numbers=number_one + number_two + number_three
product= number_one * number_two * number_three
average= sum_of_numbers / 3

if number_one >= number_two and number_one >= number_three:
	largest = number_one
elif number_two >= number_one and number_two >= number_three:
	largest = number_two
else:
	largest = number_three
if number_one <=  number_two and number_one  <= number_three:
	smallest = number_one
elif number_two <= number_one and number_two <+ number_three:	
	smallest = number_two
else:
	smallest = number_three
print(f"Sum: {sum_of_numbers}")
print(f"Average: {average}")
print(f"Product: {product}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
