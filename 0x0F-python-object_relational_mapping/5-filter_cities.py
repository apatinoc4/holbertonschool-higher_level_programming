#!/usr/bin/python3
""" 
akes in the name of a state as an argument and lists all cities
"""
from sys import argv
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities JOIN states
            ON cities.state_id=states.id WHERE states.name
            LIKE BINARY %s ORDER BY cities.id ASC""", (argv[4],))
    rows = cur.fetchall()
    result = []
    for row in rows:
        result.append(row[0])
    print(", ".join(result))
    cur.close()
    db.close()
