

# left to right pyramid
for i in range(1,10):
    for j in range(1, i+1):
        print(j, end=" ")
    print(" ")


for i in range(1, 7):
    for j in range(1, 8-i):
        print(j, end = " ")
    print(" ")


for i in range(1,7):
    print(" " * (7-(8 - i)), end=" ")
    for j in range(1,8-i):
        print(j, end="")
    print()


for i in range(1,7):
    print(" " * (7-(8 - i)), end=" ")
    for j in range(1,8-i):
        print(j, end=" ")
    print()

