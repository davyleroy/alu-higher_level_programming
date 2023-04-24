#!/usr/bin/python3
""" no injections this time! """
import sys
import MySQLdb

if __name__ == "__main__":
    with MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host='localhost',
            port=3306,
    )as conn:
        cur = conn.cursor()
        query = """ SELECT * FROM states
                    WHERE name = %s
                    ORDER BY id ASC
                """
        cur.execute(query, (sys.argv[4],))
        names = cur.fetchall()
        for name in names:
            print(name)
        cur.close()
