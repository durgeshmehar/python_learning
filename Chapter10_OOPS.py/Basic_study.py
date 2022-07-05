# (1) simple oops program
#  class number:
#     def sum(self):
#         return self.a+self.b

# num=number()  #object instantation
# num.a=17
# num.b=13
# s=num.sum()
# print(f"Sum is {s}")

#(2)Instance variable,self & learn some error
# class Employee:
#     name="XYZ"
#     company="Google"
#     salary=100000
#     print('''Company details:
#     name="XYZ"
#     company="Google"
#     salary=100000''')
    

#     def getData(self):
#         print(f"{self.name} in company {self.company} with salary {self.salary}")

# harry=Employee()
# harry.name="Harry"
# harry.salary=200000
# harry.getData()

# durgesh=Employee()
# durgesh.name="Durgesh"
# durgesh.company="Youtube"
# durgesh.getData()

# tushar=Employee()
# tushar.name="Tushar"
# tushar.getData()

# rakesh=Employee()
# print("Rakesh new not done regestration only show salary",rakesh.salary)

#(3) static method,passing many argumnet in object function call
# class Employee:
#     name="XYZ"
#     company="Google"
#     salary=100000

#     @staticmethod
#     def greet():

#         print("Good Morning !!")
#     def getData(self):
#         print(f"{self.name} in company {self.company} with salary {self.salary}")

# harry=Employee()
# harry.name="Harry"
# harry.salary=200000
# harry.greet()
# harry.getData()

#(4) __init__(argument1,argument2)  [CONSTRUCTOR]

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    company="Google"

   
    @staticmethod
    def greet():

        print("Good Morning !!")

    def getData(self):
        print(f"{self.name} in {self.company} with salary {self.salary}")

harry=Employee("Durgesh",20000)
harry.greet()
harry.getData()


