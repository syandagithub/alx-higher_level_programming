#!/usr/bin/python3
'''
lists all states with letter starting with N
'''
import MySQLdb
import sys 


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    con = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name)
    cursor = con.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%'ORDER BY id ASC")
    db = cursor.fetchall()
    for i in db:
        print(i)

    cursor.close()
    con.close()    
