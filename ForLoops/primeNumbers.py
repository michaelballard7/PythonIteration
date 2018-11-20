"""
    A prime number is a natural number greater than 1 has no positive divisors other than 1 and itself
    A natural  number greater that 1  that is not  a prime number is called a composite number

    Divide a given number with 2 to n-1 and if at any
"""

# take in a number from the user 
n = int(input("Please enter a number"))

isPrime = True

# for i in range(2, n // 2 + 1):
#     if n % 2 == 0:
#         isPrime = False
#         break

# if isPrime == True:
#     print(n, "is a prime number ")
# else: 
#     print(n, " is a composite number ")

# prime refactored

if n > 1:
    for i in range(2, n // 2 + 1):
        if n % 2 == 0:
            isPrime = False 
            break 
        if isPrime == True:
            print(n, "is a prime number")
        else: 
            print(n, "is a composite number")