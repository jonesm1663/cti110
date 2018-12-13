# 12/3/18
# CTI-110 P4HW1 - Budget Analysis
# Michael Jones
# Write a program that asks the user to enter the amount that he or she
# has budgeted for a month. A loop should then prompt the user to enter
# each of his or her expenses for the month and keep a running total.
# When the loop finishes, the program should display the amount that the
# user is over or under budget.


userbudget = float(input("Enter monthly budget:"))

moreexpenses = "y"
totalexpenses = 0

while moreexpenses == "y":
    userexpense = float(input("enter an expense:"))
    totalexpenses = totalexpenses + userexpense
    moreexpenses = input("are there more expenses?: type y for yes, n for no")

if totalexpenses > userbudget:
    print("you were over your budget",userbudget "by , totalexpense - \
          userbudget)
elif userbuget > totalexpenses:
     print("you were under your budget",userbuget "by", totalexpense - \
          userbudget)
else:
    print("you used exactly your budget of" , userbudget, ".")
    
