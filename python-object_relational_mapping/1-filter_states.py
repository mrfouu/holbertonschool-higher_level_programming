#!/usr/bin/python3
"""List all states with a name starting with 'N' from the database"""
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
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    rows = curs.fetchall()

    # Iterate over rows and print states whose name starts with 'N'
    for row in rows:
        if row[1][0] == 'N':  # row[1] refers to the name column
            print(row)
    
    curs.close()
    db.close()
