number= int(input("Enter a five-digit integer: "))
digit_one= number // 10000
digit_two= (number % 10000) // 1000
digit_three= (number % 1000) // 100
digit_four= (number % 100) // 10
digit_five= number % 10

print(f"{digit_one} {digit_two}  {digit_three} {digit_four}  {digit_five}")