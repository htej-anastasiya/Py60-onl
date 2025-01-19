import math

# task 5.1
# I'm bad at trigonometry and found in web that sin and cos in Python are calculated in radians

number_of_occurrencies = int(input("Input the number of occurencies: "))
x = int(input("Input x value: "))
x_radians = math.radians(x)
value = 0
for i in range(number_of_occurrencies):
    occurrence = pow(-1, i) * pow(x_radians, (2 * i + 1)) / math.factorial(2 * i + 1)
    value += occurrence
print("The value is: ", value)
print("The value is: ", math.sin(x_radians))

# task 5.2
number_of_occurrencies = int(input("Input the number of occurencies: "))
x = int(input("Input x value: "))
x_radians = math.radians(x)
value = 0
for i in range(number_of_occurrencies):
    occurrence = pow(-1, i) * pow(x_radians, (2 * i)) / math.factorial(2 * i)
    value += occurrence
print("The value is: ", value)
print("The value is: ", math.cos(x_radians))
