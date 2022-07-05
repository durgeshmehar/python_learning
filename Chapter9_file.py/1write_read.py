f=open("new text.txt",'w')
f.write("What in your mind what you say\n")
f.write("What in your mind bro") 
f.write("\nI am just testing") #What in your mindWhat in your mind bro

# READING OF FILES

f=open('new text.txt','r')
#(1) 
data=f.read()    #What in your mind
                    #What in your mind bro
print(data)

# data=f.readline()
# print(data)         #What in your mind
#                     #__ (space print)
#                     #What in your mind bro
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# f.close()