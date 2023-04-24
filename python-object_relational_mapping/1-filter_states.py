#!/usr/bin/python3
""" filtering stuff in here"""
import sys
import MySQLdb

if __name__ == "__main__":
    with MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host='localhost',
            port=3306
    )as conn:
        cur = conn.cursor()
        cur.execute(
                "SELECT * FROM states \
                WHERE name LIKE BINARY 'N%' \
                ORDER BY id ASC"
            )
        all_states = cur.fetchall()
        for each_state in all_states:
            print(each_state)
        cur.close()
