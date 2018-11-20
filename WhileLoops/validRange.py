"""

Write a program that can take a number from 1  to 10. If user enters number in valid range(1 to 10) then program
should display the message "Congratulations, you entered  the number in the correct range". Otherwise the program
asks the user to re-enter the number until user enters correct number.

"""


# my version: 
stillTrue = True

while(stillTrue):
    num = int(input("Please enter a number "))
    if ( num >= 1 and num <= 10):
        print("Congratulations, you entered the number in the correct range!")
        stillTrue = False
    else: 
        print("Invalid Range, Re enter the number please?")


# their version:

N = int(input("Please enter a number ?"))
while True:
    if N < 1 or N > 10:
        N = int(input("Please Re-enter a number ?"))
    else: 
        print("Congratulations, you've entered the number in the correct Range")
        break