# Relational database -lot of ram ,memory ;program store data
# in between me and my data various running program e.x. oracle,mysqlmicrosoft acess like product

# SQLLite
#store in row or column but not as spredship it as table with functionlity
# store file in binary file
#4 fundamental operation
# craate,read,update,delete
#but language offer creat,insert,select,update,delete (4 operation implement bt this keyword)
# C:\Users\durge>sqlite3
# sqlite> .mode csv
# sqlite> .import 'C:\Users\durge\Desktop\sample4.csv' shows
# 
# .schema --> table header file elemnt number
#SELECT Name FROM shows; -->read cloumn of Name 
#SELECT * FROM shows; --> all column and rows
#function like (AVG,COUNT,DISTINCT,LOWER,MAX,MIN,UPPER ...)
#USE this command for more feature
# WHERE,LIKE,ORDER BY,LIMIT,GROUP BY
#SELECT DISTINCT(Name) FROM shows; -->nor repeted
#SELECT DISTINCT((UPPER(Name)) FROM shows;  -->Uppercase word
#SELECT Name FROM shows WHERE Name="A"; -->
#SELECT Name FROM shows WHERE Name LIKE "%J%";
#SELECT DISTINCT(UPPER(Name)) FROM shows ORDER BY UPPER(Name);
#SELECT UPPER(Name),COUNT(Name) FROM shows GROUP BY UPPER(Name) LIMIT 10;

#SELECT UPPER(Name),COUNT(Name) FROM shows GROUP BY UPPER(Name) ORDER BY COUNT(Name) DESC;
#SELECT TRIM(UPPER(Name)),COUNT(Name) FROM shows GROUP BY TRIM(UPPER(Name)) LIMIT 10;

#SELECT UPPER(TRIM(Name)),COUNT(Name) FROM shows GROUP BY UPPER(TRIM(Name)) ORDER BY COUNT(Name) DESC;
#SELECT TRIM(UPPER(Name)),COUNT(Name) FROM shows GROUP BY TRIM(UPPER(Name)) ORDER BY COUNT(Name) DESC LIMIT 10;
#.save file_name.db

###########################
#SELECT Name FROM shows WHERE UPPER(Meme)=UPPER("Durgesh");
#SELECT Name FROM shows WHERE Meme LIKE "%Durgesh%";
#SELECT Meme FROM shows;
#SELECT Name FROM shows WHERE Meme LIKE "%vansh%";
#SELECT Game FROM shows WHERE Meme LIKE "%vansh%";
#SELECT Meme FROM shows WHERE Meme LIKE "%vansh%";
# SELECT * FROM shows WHERE Meme LIKE "%Durgesh";
#Insert Into shows (Game,Name,Meme) VALUES("40", "z", "Kalpana");
#SELECT * FROM shows WHERE Meme LIKE "%Kalpana%";
#SELECT * FROM shows WHERE Meme LIKE "%alpan%";
#UPDATE shows SET Game="35" WHERE Meme="Kalpana";
#DELETE FROM shows WHERE Name LIKE "z";
#
#sqllite 5 main datatypes
#1)BLOB 2)INTEGER 3)NUMERIC 4)REAL 5)TEXT
##
#????????????
#To save file in database
#m^c
#mv shows.db .shows.db  ?now left with original data
#SELECT * FROM Name;

#SELECT * FROM Meme;
#SELECt show_id FROM Meme WHERE Mem ="Mehar";
#SELECT Name FROM shows WHERE id IN (SELECT show_id FROM Meme WHERE Mem ="Mehar");
#SELECT ID from shows WHERE Name="D";
#SELECT Meme from shows WHERE Name="D";
# SELECT DISTINCT(Mem) FROM Meme WHERE show_id In (SELECT id from shows WHERE Name="A") ORDER BY Mem; 
#SELECT DISTINCT(UPPER(Mem)) FROM Meme WHERE show_id In (SELECT id from shows WHERE Name="A") ORDER BY Mem;

#SELECT DISTINCT(UPPER(Mem)) FROM Meme WHERE show_id In (SELECT id from shows WHERE Name="A") ORDER BY upper(Mem); 

#CREATE INDEX title_index ON shows(title);

#.timer on #.timer off

#(1)#SELECT id FROM people WHERE name="Steve Carell";
#(1)#SELECT person_id from stars where person id=(SELECT id FROM people WHERE name="Steve Carell");
#(1)#SELECT id FROM shows WHERE id=(SELECT person_id from stars where person id=(SELECT id FROM people WHERE name="Steve Carell"));

# OR
# (Time more running)(time=0.56)
#sqlite> SELECT title FROM people
#   ...> JOIN stars ON people.id=stars.person_id
#   ...> JOIN shows ON stars.show_id=show.id
#   ...> WHERE name="Steve Carell"
# (Then we created indexes to run fast)(time=0.001)

#(2)#CREATE INDEX star_index ON star(person_id);

#(2)#CREATE INDEX show_index ON stars(show_id);

#(2)#CREATE INDEX name_index ON people(name);
# &&&&&&&&&&
# sql injection
# wrong-way
# rows=db.execute(f"SELECT * FROM user WHERE username='{username}' AND password='{password}'")
# if len(rows)==1;   #If condition true,now user login 
#(reason as enter durgehsjj@746'--then username='durgehsjj@746'--' now confusion in ' 'so)



#Correct way
#rows=db.execute(SELECT * FROM user WHERE username=? AND password=?,username,password)
# if len(rows)==1;   #If condition true,now user login

#Race Condition
#(database program to increase,update like by cs 50)

#rows= db.execute("SELECT likes FROM posts WHERE id=?",id);
#likes=rows[0]["likes"]
#db.execute("UPDATE posts SET likes=? WHERE id =?",likes+1,id)

#(sometimes database confused when at same time updatation of two like but add one each time so use TRANSACTION feature to to first one task then next like)

#db.execute("BEGIN TRANSACTION")
#rows= db.execute("SELECT likes FROM posts WHERE id=?",id);
#likes=rows[0]["likes"]
#db.execute("UPDATE posts SET likes=? WHERE id =?",likes+1,id)
#db.execute("COMMIT")