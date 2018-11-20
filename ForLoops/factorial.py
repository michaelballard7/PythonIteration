
# n = 5
# for i in range(1,n-1):
#     fac = i * (n-i)
#     print(fac)

""" 
    1. Take the value of N
    2. Set F = 1 
    3. Repeat a counter = 1 to N
        Calculate f = f * counter 
    4. Display the value of F to the screen
"""


n = int(input(" What factorial do you want?"))
f = 1 
for i in range(1, n+1):
    f = f * i 
    print(f)  

