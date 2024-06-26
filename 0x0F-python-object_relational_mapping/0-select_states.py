#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306
    )

    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id')

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
