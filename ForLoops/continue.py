
""" The Continue statement will move control to the next iteration and skip all statements that come after continue """

for i in range(1,101):
    if i % 3 == 0:
        continue 
    else:
        print(i)