class Employee:
    salary=20000
    increment=1.5

    @property 
    def totalSalary(self):
        return self.increment*self.salary

    @totalSalary.setter
    def totalSalary(self,val):
        self.increment=val/self.salary



E1=Employee()
print(E1.salary)
print(E1.increment)
print(E1.totalSalary)
E1.totalSalary=40000
print(E1.salary)
print(E1.increment)
print(E1.totalSalary)


