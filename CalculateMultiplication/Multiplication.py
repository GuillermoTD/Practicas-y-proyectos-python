#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

number_one = int(input("Ingrese el number_one  "))
number_two = int(input("Ingrese el number_two  "))
product = number_one * number_two
sum = 0

if number_one % number_two <= 1000:
    print(f"The result is: {product}")
else:
    sum = number_one + number_two
    print(f"There is no number that it's product is lower or equal than 1000", sum)
