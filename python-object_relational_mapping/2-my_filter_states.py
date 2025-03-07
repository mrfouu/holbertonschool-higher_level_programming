#!/usr/bin/python3
"""Display all states from the states table where the name matches the argument."""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )

    curs = db.cursor()
    state_name = sys.argv[4]
    curs.execute("SELECT * FROM states WHERE name = '{}' "
                 "ORDER BY id ASC".format(state_name))
    row = curs.fetchall()

    for row in curs:
        if row[1] == sys.argv[4]:
            print(row)
    curs.close()
    db.close()
