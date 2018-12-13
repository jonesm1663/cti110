#cti 110
#p3t1
#Michael Jones
#11/13/18
#ask user for size
#of the rectangle
lengthA=int(input("lengthA?"))

widthA=int(input("widthA?"))

areaA=lengthA*widthA
#areaB=(lengthB*widthB)
print("areaA is",areaA)

lengthB=int(input("lengthB?"))
widthB=int(input("widthB?"))
areaB=lengthB*widthB
print("areaB is",areaB)
            
                  
if areaA>areaB:
    print("A is larger")
elif areaA==areaB:
    print("areaA is the same as areaB")
    
else:
    print("B is larger")

