#!/usr/bin/env python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import argparse
import MySQLdb

def list_states(user, password, database):
    try:
        db = MySQLdb.connect(user=user, passwd=password, db=database, port=3306)
    except MySQLdb.Error as e:
        print(f"Error connecting to database: {e}")
        return
    
    cur = db.cursor()
    cur.execute("SELECT name FROM states;")
    states = cur.fetchall()

    for state in states:
        print(state[0])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='List all states from a database.')
    parser.add_argument('user', help='Database username.')
    parser.add_argument('password', help='Database password.')
    parser.add_argument('database', help='Database name.')
    args = parser.parse_args()

    list_states(args.user, args.password, args.database)
