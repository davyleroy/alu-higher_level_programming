#!/usr/bin/python3
""" filters states according to input """
import sys
import MySQLdb

if __name__ == "__main__":
    with MySQLdb.connect(
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                host='localhost',
                port=3306
    )as engine:
        cur = engine.cursor()
        cur.execute(
                "SELECT * FROM states \
                 WHERE name LIKE BINARY'{}'".format(sys.argv[4]))
        all_states = cur.fetchall()
        for each in all_states:
            print(each)
        cur.close()
