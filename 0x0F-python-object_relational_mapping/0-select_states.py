#!/usr/bin/python3

import MySQLdb
import sys

"List all the states from the table"

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    state = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.Close()
