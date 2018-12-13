# cti-110
# 12/6/18
# P4HW2  
# Michael Jones
# Celsius to Fahrenheit Table

#F=(9/5)C+32

print("celsius\tfahrenheit")
for celsiustemperature in range( 21 ):
    fahrenheittemperature = ( 9/5 )*celsiustemperature+32
    print(celsiustemperature,"\t",format(fahrenheittemperature,".2f"))
    
