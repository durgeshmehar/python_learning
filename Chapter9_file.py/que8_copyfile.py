# with open("new text.txt","r") as f:
#     content=f.read()
# with open("copy.txt","w") as fp:
#     fp.write(content)
# print(content)

# que(9) check content of file is same or not
# with open("new text.txt","r") as f:
#     content1=f.read()
# with open("copy.txt","r") as fp:
#     content2=fp.read()
# if content1==content2:
#     print("Both files has same data")
# else:
#      print("Different data in both files")

# que(10) wipe out data of file
# with open("copy.txt","w") as f:
#     f.write("")

# que(11) rename file as

import os
oldname="oldname.txt"
newname="rename_by_python.txt"

with open(oldname,'r') as f:
    content=f.read()
with open(newname,'w') as f:
    f.write(content)
os.remove(oldname)


