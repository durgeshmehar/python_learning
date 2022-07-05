li=[3,8,89,67]    
print(li)        #[3, 8, 89, 67]
print(li[0])     #3
li[1]=li[1]+5

#li=li[1:3]
#print(li)    #or
print(li[1:3])    #[13,89]


li=[3,2,1,8,89,67,0.5]
li.sort()
print(li)            #[0.5, 1, 2, 3, 8, 67, 89]
print("length:",len(li))   #length: 7
li.append(45)
print(li)               #[0.5, 1, 2, 3, 8, 67, 89, 45]
li.insert(0,785)

print(li)         #[785, 0.5, 1, 2, 3, 8, 67, 89, 45]
print("pop function\n")
li.pop()         #last value delete
print(li)        #[785,0.5, 1, 2, 3, 8, 67, 89] 
li.remove(0.5)
print(li)         #[785, 1, 2, 3, 8, 67, 89]
li.sort()
print(li)        #[1, 2, 3, 8, 67, 89, 785]
li.reverse()
print(li)     #[785, 89, 67, 8, 3, 2, 1]

'''##################'''
t=(3,4,5,6,3,"durgesh",3,"durgesh")
print(t[0])   #3
print(t[3])   #6
print(t.count(3)) #3
print(t.count("durgesh"))  #2
print(t.index(5))        #2
print(len(t))            #8
