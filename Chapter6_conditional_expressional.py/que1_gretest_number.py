num1=int(input("Enter first number\n"))
num2=int(input("Enter second number\n"))
num3=int(input("Enter third number\n"))
num4=int(input("Enter fourth number\n"))
# if(num1>num2):
#     if(num1>num3):
#         if(num1>num4):
#             print("Num 1=",num1," is gretest")
#         else:
#             print("Num 4=",num4," is gretest")    
        
#     else:
#         if(num3>num4):
#             print("Num 3=",num3," is gretest")
# else: #num2 >num1
#     if(num2>num3):
#         if(num2>num4):
#             print("# Num 2=",num2," is gretest")
#     else:  #num3>num2
#         if(num3>num4):
#             print("# Num 3=",num3," is gretest")
#         else:
#             print("# Num 4=",num4," is gretest")

##########or or or or or or or or or or or#####
if(num1>num2):
    f1=num1
else:
    f1=num2
if(num3>num4):
    f2=num3
else:
    f2=num4
if(f1>f2):
    print("gretest number is ",f1)
else:
    print("gretest number is ",f2)

  