# indivudual count the repeat word
import csv
title = input("Title: ").strip().upper()
with open("./sample4.csv","r") as file:
    reader = csv.DictReader(file)
    counter = 0
    for row in reader:
        if row["Name"].strip().upper()==title:
            counter +=1
print("Counter: ",counter)