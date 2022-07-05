# (1) Exit
# import sys
# if len(sys.argv)!=2:
#     print("Missing argument !")
#     sys.exit(1)
# print(f"hello,{sys.argv[0]}")
# sys.exit(0)

#(2) Command line
# from sys import argv
# for arg in argv:
#     print(arg)
#or
# if len(argv)==2:
#     print(f"Hello, {argv[1]}")
# else:
#     print("Hello,world")

#(3) Number search
# import sys
# numbers=[2,3,4,5,6,7,0]
# if 1 in numbers:
#     print("Found")
# else:
#     print("Not found")
# print("********* ******")

# names=["bill","durgesh","hrushi","Ganna"]

# if "Hrushi" in names:
#     print("Found")
# else:
#     print("Not")

# (4)
# Dictioary
# from cs50 import get_string

# people={"Brian":"+9192888747","Durgesh":"9823072134",5:8}
# # a=Durgesh
# a=get_string("Enter :")
# # print(f"{a} mobile no: {people[a]}")  #only cs50 library
# print(f"{a} mobile no: {people.get(a)}")  
  
# print(people.keys())
# print(people.values())

#(5)
x=1
y=2
print(f"x is {x},y is {y}")
x,y=y,x
print(f"x is {x},y is {y}")






