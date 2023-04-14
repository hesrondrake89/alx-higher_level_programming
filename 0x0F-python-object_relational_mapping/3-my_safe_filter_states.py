#!/usr/bin/python3
"""
Safely retrieves all values from the states table 
in a database where the name column matches the provided argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s;", (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state)