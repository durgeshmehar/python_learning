class Complex:
    def __init__(self,r,i):
        self.real=r
        self.img=i
    def __add__(self,c):
        return Complex(self.real+c.real,self.img+c.img)

    def __mul__(self,c):
        mulReal=self.real*c.real-self.img*c.img
        mulImg=self.real*c.img+self.img*c.real
        return Complex(mulReal,mulImg)

    def __str__(self):
        if self.img<0:
            return f"{self.real}-{-self.img}i"
           
        else:
           return f"{self.real}+{self.img}i"

    
c1=Complex(1,-4)
c2=Complex(3,-8)
c=c1+c2
print(c)
print(c1*c2)