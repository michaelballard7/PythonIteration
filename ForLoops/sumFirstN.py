"""
    Write a program to take an integer  number N from user. Calculate and displays the sum of numbers from 1 to N
""" 

# num = int(input("Please enter a number"))

# for i in range(1,num +1):
#     series = (i(i+1)/2)
#     print(series)



SUM = 0 
n = int(input("Please give a number"))

for num in range(1,n+1):
    SUM +=  num

print(SUM)

