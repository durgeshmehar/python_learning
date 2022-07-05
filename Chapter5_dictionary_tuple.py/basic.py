'''
Dictionary 
dic={
    "home" : "shioni",
    "college" : "pune",
    "marks":[20,40,60],
    "relative" :{'pachgaon':'neri'},
    "college":"Shahapur",
    5:8,
    "list":"[2,3,45,6]"
}
print("\n")
print(dic)
print("\n")
print(list(dic.values()))
print(list(dic.keys()))
print(dic[5])
print(dic['college'])
print(dic['relative']["pachgaon"])
print("\n")
print(dic.keys())
print(type(dic.keys()))
print("\n")
print(dic.values())
print(type(dic.values()))
print("\n")
print(dic.items())
print("\n")
updatedict={
    "name1":'durgesh',
    "name1":'ganesh',
    "va":"d1",
    "vab":"d1",
}
dic.update(updatedict)
#print(dic)
dic.update({"name":"vijay"})
print(dic)
print(dic.get("name1"))
#print(dic["name3"])        #error 
'''

#set
s={2,6,6,9,68,6}
m={}
print(type(s))      #<class 'set'>
print(type(m))      #<class 'dict'>
s.add(4)
s.add(4)
s.add(5)
print(s)
s.remove(68)
print(s)

s.pop()      #it remove first element
print(s) 
t={2,6,7,1,3,4,5}
z=t.union(s)
y=t.intersection(s)
print(z)
print(y)

