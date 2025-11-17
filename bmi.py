weight= float(input("Enter weight(kg): "))
height= float(input("Enter height(metres): "))

bmi= weight/(height*height)
if bmi <18.5:
	print ('Underweight')
if bmi >18.4 and bmi < 25.0:
	print ('Normal')
if bmi >24.9 and bmi< 30.0:
	print('Overweight')
if bmi >30 or bmi == 30:
	print('Obese')
