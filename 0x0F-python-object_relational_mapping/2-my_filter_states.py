#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()
    cursor.execute(f"""SELECT * FROM states WHERE name LIKE BINARY
     '{sys.argv[4]}'""")
    rows = cursor.fetchall()
    for row in rows:
        print(rows)
    cursor.close()
    db.close()
