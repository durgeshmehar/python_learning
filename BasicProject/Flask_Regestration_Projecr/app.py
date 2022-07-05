import os
from flask import Flask,render_template, request,redirect
from cs50 import SQL
from flask_mail import Mail, Message

app= Flask(__name__)
app.config["MAIL_DEFAULT_SENDER"]="durgeshmehar2002@gmail.com"
app.config["MAIL_PASSWORD"]="ognsbyhaybibrbsc"
app.config["MAIL_PORT"]=587
app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_USE_TLS"]=True
app.config["MAIL_USERNAME"]="durgeshmehar2002@gmail.com"
mail=Mail(app)


#Database Information
open("froshims.db","w").close()
db = SQL("sqlite:///froshims.db")
db.execute("CREATE TABLE registrants (id INTEGER, name TEXT NOT NULL,email TEXT NOT NULL, sport TEXT NOT NULL,PRIMARY KEY(id))")

#Sport List
SPORTS=["Cricket","basket-ball","Carrom","Hockey","Swimming"]

#Route Information
@app.route("/")
def index():
    return render_template("index.html",sports=SPORTS)

@app.route("/register",methods=["POST"])
def register():
    name=request.form.get("name")
    if not name:
        return render_template("error.html",message="Missing Name")
    sport=request.form.get("sport_all")
    email=request.form.get("email")
    if not email:
        return render_template("error.html",message="Missing Email")
    if not sport:
        return render_template("error.html" ,message="Missing to select Sport")
    if sport not in SPORTS:
        return render_template("error.html",message="Invalid Sport")
    def basic_first_ido():
       '''return render_template("success.html",name=request.form.get("name"),sport=request.form.get("sport_all"))

        if not request.form.get('name') or request.form.get('sport_all') not in SPORTS:
         return render_template("success.html")
        return render_template("success.html")'''
    db.execute("INSERT INTO registrants (name,email,sport) VALUES (?,?,?)",name,email,sport)

    message=Message(f"Congratulation, You are Registered ! as name {name} with sport {sport} Thank you  Enjoy your day.",recipients=[email])
    mail.send(message)

    return redirect("/registrants")

@app.route("/registrants")
def registrant():
    registrants=db.execute("SELECT * FROM registrants")
    return render_template("registrants.html",regi=registrants)

#Running condition
if __name__=="__main__":
    app.run(debug=True)