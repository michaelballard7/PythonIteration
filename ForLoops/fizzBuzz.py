""" Write a program that can display the numbers from 1 to 100 which are not multiples of 3 and 5 """


for i in range(1,101):
    if i % 15 == 0:
        print( "Fizz buzz")
        continue 
    elif i % 5 == 0:
        print( "Fizz")
        continue
    elif i % 3 == 0:
        print("Buzz")
        continue
    else: 
        print(i)


