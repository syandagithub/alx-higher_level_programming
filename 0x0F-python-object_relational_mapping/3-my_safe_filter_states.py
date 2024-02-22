#!/usr/bin/python3
'''lists all states from the database'''
import MySQLdb
import sys 


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    statename= sys.argv[4]

    cont = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name)
    cursor = cont.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", (statename,)
        )
    db = cursor.fetchall()
    for i in db:
        print(i)
