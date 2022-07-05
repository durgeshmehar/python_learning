with open ('new text.txt','w') as fp:
    fp.write("me as brother")
with open('new text.txt','a') as fp:
    fp.write(" I am appending")
with open ('new text.txt','r') as fp:
    a=fp.read()    
    print(a)
