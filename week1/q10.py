celsius = float(input("Enter temperature in celcius"))

fahrenhit = celsius*9/5+32
print("Temperature in Fahrenheit:",fahrenhit)
if(celsius<0):
    print("very cold wear thick jacket")
elif(celsius>=0 and celsius<=15):
    print("cold wear jacket")
elif(celsius>=16 and celsius<=25):
    print("nice weather")
else:
    print("hot! stay hydrated")