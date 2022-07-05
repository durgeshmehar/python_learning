'''class university:
    location="India"
    name="DY Patil"
    def gamemiddle(self):
        print("Start now film is not end")

class pcmc(university):
    rule="Strictly antiragging"
    help="Call 9823101319"
    def gamestart(self):
        super().gamemiddle()
        print("Middle but not start")


class dypune(pcmc):
    location="pune"
    student="durgesh & 1500"
    fee=70000
    aim="Gain knowledge upto last"
    def info(self):
        super().gamestart()
        print("Last but not least")

c1=dypune()
c1.info()
'''

'''class university:
    location="India"
    name="DY Patil"
    def __init__(self):
        print("Start now film is not end")

class pcmc(university):
    rule="Strictly antiragging"
    help="Call 9823101319"
    def __init__(self):
        super().__init__()
        print("Middle but not start")


class dypune(pcmc):
    location="pune"
    student="durgesh & 1500"
    fee=70000
    aim="Gain knowledge upto last"
    def __init__(self):
        super().__init__()
        print("Last but not least")

c1=dypune()'''
'''
class dypune():
   
    student="durgesh & 1500"
    fee=70000
    @classmethod
    def change(cls,new):
        cls.fee=new

student1=dypune()
student1.change(50000)
print(student1.fee)
print(dypune.fee)
'''

'''
# (incapsulation)
class Employee:
    salary=20000
    bonus=5000

    @property
    def totalSalary(self):
        return self.salary+self.bonus

    @totalSalary.setter
    def totalSalary(self,new):
        Employee.bonus=new-Employee.salary
        

        


e=Employee()
print(e.totalSalary)
e.totalSalary=30000
print(Employee.salary)
print(Employee.bonus)

'''
'''
#  OVERLODING CONCEPT

class Number:
    numb=5
    def __init__(self,num):
        self.numb=num

    def __add__(self, num2):
        print("Lets add")
        print("hiii")
        return self.numb + num2.numb

n1= Number(3)
n2= Number(4)
n3=n1+n2     #n3.add(3,4)
print(n3)
'''
'''
class Number:
    def __init__(self,num):
        self.num=num  

    def __str__(self):
        return f"Number is {self.num}"

r= Number(5)
print(r)
'''
