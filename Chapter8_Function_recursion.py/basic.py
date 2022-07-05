#(1)
# def greeting(name="Jaggu"):
#     print("GOOD MORNING, "+name)
#     return name

# n=greeting("Durgesh")
# print(n)
# n=greeting()
# print(n)


def factorial(num):
    if(num==0 or num==1):
        return 1
    else:
        return num*factorial(num-1)
user_num=int(input("Enter number\n")) 
b=factorial(user_num)
print("factorial of b=",user_num,"is",b)
    