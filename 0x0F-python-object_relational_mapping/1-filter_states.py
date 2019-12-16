#!/usr/bin/python3
""" lists all states with a name starting with N (upper N)  """
from sys import argv
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY
                'N%' ORDER BY states.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
    