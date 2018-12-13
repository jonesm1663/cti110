# CTI-110 
# P3HW2 - Shipping Charges 
# Michael Jones 
# 12/2/18

#write a program tha asks the user to enter the weight of a package
#then display shipping charges

weightofpackage = int(input("Please enter the weight of the package:"))
if weightofpackage<= 2:
    shippingcharges = 1.50
elif weightofpackage < 7:
    shippingcharges = 3.00
elif weightofpackage < 11:
    shippingcharges = 4.00
else:shippingcharges = 4.75

print("package weighs"+str(weightofpackage)+", you pay"+ \
      format(shippingcharges,",.2f"))
    

