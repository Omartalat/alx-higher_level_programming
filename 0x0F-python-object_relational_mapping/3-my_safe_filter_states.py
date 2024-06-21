#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""
import MySQLdb
import sys

db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306
        )

cursor = db.cursor()

cursor.execute('SELECT * FROM states')

states =cursor.fetchall()

for state in states:
    if state[1] == sys.argv[4]:
        print(state)     

cursor.close()
db.close()
