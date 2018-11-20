
# Do not forget to convert the number type
number = int(input("Please enter a number"))

for i in range(1,11):
    result = number * (1+i)
    print(number, "x", i, "=", result)