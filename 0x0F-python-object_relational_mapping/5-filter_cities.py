#!/usr/bin/python3
"""
lists all cities from the database
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":

   


    cont = 0
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    query_rows = cursor.fetchall()
    for row in query_rows:
        if row[2] == argv[4]:
            if cont > 0:
                print(", ", end="")
            print(row[1], end="")
            cont = cont + 1
    print()
    cursor.close()
    db.close()
