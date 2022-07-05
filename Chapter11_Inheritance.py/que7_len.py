class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        str1=""
        index=0
        for i in self.vec:
            str1+=f"{i}a{index} +"
            index+=1
        return str1[:-1]
    def __add__(self,vec2):
        newList=[]
        for i in range(len(self.vec)):
            newList.append(self.vec[i]+vec2.vec[i])
        return Vector(newList)

    def __mul__(self,vec2):
        sum=0
        if(len(self.vec)==len(vec2.vec)):
           for i in range(len(self.vec)):
               s=self.vec[i]*vec2.vec[i]
               sum=sum+s
           return sum
        else:
            return "You can't multiply as not length same"
    def __len__(self):
        return len(self.vec)

v1=Vector([1,4])
v2=Vector([3,6,8])
print((v1+v2))
print(v1*v2)
print(len(v1))
print(len(v2))
