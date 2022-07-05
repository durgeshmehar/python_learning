num=int(input("Enter number\n"))
fact=1
for i in range(1,num+1,1):
    fact=fact*i
print(f"Factorial of {num} is {fact}")