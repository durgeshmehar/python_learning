num=int(input("Enter the number :"))
prime=True
for i in range(2,num,1):
    if(num%i==0):
        prime=False
        break
if prime:
    print("Prime number is ",num)
else:
    print("wrong it is not Prime number is ",num)
