#(1) def table(num):
#     for i in range(1,11):
#         print(f"{num} x {i}= {num*i}")

# n=int(input("Enter the number:"))
# print("Multiplication table of",n)
# table(n)

#(2)Method without using loop
def multiplication(num,i):
    if(i<11):
        print(f"{num} * {i}={num*i}")
        return multiplication(num,i+1)
    else:
        return i*4

m=multiplication(16,1)
print(m)
