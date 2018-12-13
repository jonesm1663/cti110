# CTI-110 
# P3HW1 - Roman Numerals 
# Michael Jones 
# 12/2/18

#Write a program that prompts the user to enter a number within the range of 1-10
#The program should display the Roman numeral version of that number.
#If the number is outside the range of 1-10, the program should display as error message.


userNumber = int(input("Please enter a number"))
if userNumber ==1:
    print("1")
elif userNumber ==2:
    print("II")
elif userNumber ==3:
    print("III")
elif userNumber ==4:
    print("IV")
elif userNumber ==5:
    print("V")
elif userNumber ==6:
    print("VI")
elif userNumber ==7:
    print("VII")
elif userNumber ==8:
    print("VIII")
elif userNumber ==9:
    print("IX")
elif userNumber ==10:
    print("X")
else:
    print("Error: Please enter a number between 1 and 10.")
