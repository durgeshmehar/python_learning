from cs50 import SQL
import csv
from flask import Flask, redirect,render_template, request,session
from flask_session import Session

open("book.db","w").close()
db =SQL("sqlite:///book.db")
db.execute("CREATE TABLE book (id INTEGER,Name TEXT,PRIMARY KEY(id))")

with open("sample4.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        Name=row["Name"].strip().upper()
        id=db.execute("INSERT INTO book (Name) VALUES(?)",Name)

app=Flask(__name__)
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)


@app.route("/")
def index():
    books=db.execute("SELECT * FROM book")
    return render_template("index.html",books=books)

@app.route("/cart", methods=["GET","POST"])
def cart():
    if "cart" not in session:
        session["cart"]=[]
    #post value
    if request.method=="POST":
        id=request.form.get("id")
        session["cart"].append(id)
        redirect("/cart")
    #get  value
    books=db.execute("SELECT * FROM book WHERE id in (?)",session["cart"])
    return render_template("cart.html",books=books)
 
if __name__=="__main__":
    app.run(debug=True)

    
    




