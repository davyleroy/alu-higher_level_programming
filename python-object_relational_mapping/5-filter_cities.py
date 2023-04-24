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
        query = """ SELECT cities.name
                    FROM states
                    INNER JOIN cities ON states.id = cities.state_id
                    WHERE states.name = '{:s}'
                    ORDER BY cities.id ASC
                """
        cur.execute(query.format(sys.argv[4]))
        cities = cur.fetchall()
        print(", ".join([city[0] for city in cities]))
        cur.close()
