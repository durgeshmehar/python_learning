# with open("bad.txt",'r') as p:
#     word=p.read()
# word=word.replace("lazy donkey","#$%^&$##")
# with open("bad.txt",'w') as p:
#     p.write(word)
# print("Success")

# (que5)BY USING LIST REPLACE

badwords=["donkey","lazy","mad"]
with open("bad.txt",'r') as p:
    content=p.read()
    for word in badwords:
        content=content.replace(word,"#$%^&$##")
with open("bad.txt",'w') as p:
    p.write(content)
print("Success")