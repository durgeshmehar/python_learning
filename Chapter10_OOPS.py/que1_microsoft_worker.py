class Programmer:
    company="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getInfo(self):
        print(f"Employee name:{self.name} ,work as :{self.product}")
    
harry=Programmer("Harry","Github")
durgesh=Programmer("Durgesh","BackEnd")

harry.getInfo()
durgesh.getInfo()



