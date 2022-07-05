#csv store comma seperated value, it not meangfully store large data as for google,youtube facebook
#it is storing way of data in tabular form,quickly sorted.
#flat-file database is store the any data
#csv file save data only static,not changeble means not uses formulae like in excel
#ex. csv, txt or tsv or binary file 
import csv

with open("./sample4.csv","r") as file:
    reader = csv.reader(file)
    next(reader)       #skip the header of file
    
    for row in reader:
        print(row[0]," " ,end="")
        print(row[1])
        
       
# import csv
# with open("./sample4.csv","r") as file:
#     reader = csv.DictReader(file)
#     print(reader.fieldnames)
#     # for row in reader:
#     #     print(row)
     
# import csv

# titles = set()
# with open("./sample4.csv","r") as file:
#     reader = csv.DictReader(file)
#     for row in reader: 
#         titles.add(row["Name"].strip().upper())
        
# for Name in sorted(titles):
#     print(Name)
      
# import csv

# titles = {}
# with open("./sample4.csv","r") as file:
#     reader = csv.DictReader(file)
#     for row in reader: 
#         # print(f"(1)dictionary:{titles}")

#         no_repeat=row["Name"].strip().upper()

#         # print("add: ",no_repeat)
#         # print(f"(1)dictionary:{titles}")
#         if no_repeat not in titles:
#             titles[no_repeat] =0
#         titles[no_repeat] = titles[no_repeat]+1

#         # print("1::",titles[no_repeat])
#         # print("2::",titles[no_repeat])

#     print("titles:",list(titles.keys()))      

# def f(no_repeat):
#     return titles[no_repeat]

# for Name in sorted(titles, key=lambda no_repeat: titles[no_repeat], reverse=True): #or
# # for Name in sorted(titles, key=f, reverse=True):
#     print(Name,titles[Name])
        
        

