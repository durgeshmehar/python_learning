class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        str1=""
        str1=f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
        return str1
    
c1=Vector([1,2,3])
c2=Vector([9,8,6])
print(c1)
print(c2)