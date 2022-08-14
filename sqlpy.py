import sqlite3 as sql 

username = ""
password = ""

con = sql.connect('testdb.db')
cur = con.cursor()
statement = "SELECT username, password FROM users"

cur.execute(statement)
print(cur.fetchall())

loginstatement = "SELECT username, password FROM users WHERE username='{}' AND password='{}';".format(username, password)
cur.execute(loginstatement)

if not cur.fetchone():
    print("Login Failed")
else:
    print("Welcome")

# addstatement = "INSERT into users VALUES ('test','test1');"
# cur.execute(addstatement)
# con.commit()
# print(cur.lastrowid)

# https://compucademy.net/user-login-with-python-and-sqlite/
# https://www.sqlitetutorial.net/sqlite-python/insert/
# use db browser for sqlite for debugging/testing 

# setup:
# CREATE TABLE IF NOT EXISTS “users” (
# “username” TEXT,
# “password” TEXT
# );
# INSERT INTO “users” VALUES (‘boss’,’1234′);
# INSERT INTO “users” VALUES (‘admin’,’password’);