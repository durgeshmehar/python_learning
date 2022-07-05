import csv
from cs50 import SQL

open("shows.db","w").close()
db =SQL("sqlite:///shows.db")
db.execute("CREATE TABLE shows (id INTEGER,Game INTEGER,Name TEXT,PRIMARY KEY(id))")
db.execute("CREATE TABLE Meme (show_id INTEGER, Mem TEXT, FOREIGN KEY(show_id) REFERENCES shows(id))")


with open("./sample5.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        Name=row["Name"].strip().upper()
        Game=row["Game"]
        
        id=db.execute("INSERT INTO shows (Name,Game) VALUES(?,?)",Name,Game)
        for Mem in row["Meme"].split(", "):
            db.execute("INSERT INTO Meme(show_id,Mem) Values(?,?)",id,Mem)

print(db.execute("SELECT * FROM Name"))

