import sqlite3 as sq


with sq.connect("db.sqlite3") as con:
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS test(id INT, nick TEXT, wins INT, loses INT)")

    cur.execute("INSERT INTO test VALUES(1, 'Max', 2, 0)")