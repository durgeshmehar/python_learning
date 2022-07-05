#inside set can we change list values

# s={8,7,12,"durgesh",[1,2]}     #error:unshable list(mutable)
# t={8,7,12,"durgesh",(1,2)}

u={56,47,212,"gesh",{3:4}}     #error:unshable dict(mutable/changable)in hashable->
                               # (unchangeble) set

# print(s)  #list are unhasheable.so eror:unhashable

# print(t)  #give output not change value inside tuple(hashed)
print(u)