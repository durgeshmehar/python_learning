# class Calculator:
#     def square(self):
#         print("Square :",self.a**2)

#     def cube(self):
#         print("cube :",self.a**3)

#     def square_root(self):
#         print("Square-root :",self.a**0.5)
    
# num=Calculator(4)
# num.a=int(input("Enter Number :\n"))
# num.square()
# num.cube()
# num.square_root()

# que(3) //does change value in class operator by object instance
class Sample:
    a="Viju"
obj=Sample()
obj.a="Durgesh"
print(Sample.a)   #Viju
print(obj.a)      #Durgesh
#change by following
Sample.a="Mukunda"
print(Sample.a)  #Mukunda