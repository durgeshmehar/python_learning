def remove_and_split(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()


p="      Durgesh Bhai   "
n=remove_and_split(p,"Durgesh")  #Bhai
print(n)
# print(p)                 #      Durgesh Bhai   
# print(p.strip())         #Durgesh Bhai
