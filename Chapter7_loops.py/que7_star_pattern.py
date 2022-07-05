n=3

for i in range(4):     #*
                       #**
                       #***
                       #****
    print("*"*(i+1)) 
# que 8
m=3
for j in range(3):
    print(" "*(m-j-1),end="")
    print("*"*(2*j+1),end="")
    print(" "*(m-j-1))
# que 9
m=3
for i in range(3):
    print("* "*m)