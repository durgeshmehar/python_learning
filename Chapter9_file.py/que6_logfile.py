# with open("log.txt") as f:
#     content=f.read()   #f.read.lower()
# if "python" in content.lower():
#     print("It is present")
# else:
#     print("It's absent")

# QUE(7):Line number of name
content=True
i=0
with open("log.txt") as f:
    
    while content:
       content=f.readline()   #f.read.lower()
       
       i=i+1
       if "python" in content.lower():
        #    print(content)
           print(f"python is present in line {i}")
    
           

   

 