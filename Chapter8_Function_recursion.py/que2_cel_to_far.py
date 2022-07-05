def max(num1):
    far=32+(9.0/5.0)*num1
    return far
    

print("celsius to faranaheit program\n")
num1=int(input("Enter celsius temperature :\n"))
z=max(num1)

z_round="{:.2f}".format(z)
print("Temperature in faranaheit is",z_round)

#que3
#prevent to print in python in next line
print("end",end="")
print(" Thanks")