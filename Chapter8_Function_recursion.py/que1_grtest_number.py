def max(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            print("Number 1 :",num1,"Is gretest")
        else:
            print("Number 3 :",num3,"Is gretest")
    else:
        if(num2>num3):
            print("Number 2 :",num2,"Is gretest")
        else:
            print("Number 3 :",num3,"Is gretest")

print("Gretest number program\n")
num1=int(input("Enter number 1 :"))
num2=int(input("Enter number 2 :"))
num3=int(input("Enter number 3 :"))
max(num1,num2,num3)