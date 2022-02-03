import cgi
import sqlite3
import time

conn=sqlite3.connect('database.db')
c=conn.cursor()

c.execute("SELECT temperature, humidite, date FROM releves")
L = c.fetchall()

for line in L:

form = cgi.FieldStorage()
print("content-type: text/html; charset=iso-8859-1\n")

#while 1:
html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="./style.css">
    <title>titre</title>
</head>
<body>
    <h1>Météo</h1>""" + str(L) + """
</body>
</html>
"""

print(html)
    #time.sleep(1)