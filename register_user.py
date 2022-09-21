import sqlite3

dbname = 'main.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('INSERT INTO users(full_name, nick_name) values("池田紅葉", "いけだくれは")')
cur.execute('INSERT INTO users(full_name, nick_name) values("卜穎剛", "ぼくえいごう")')
cur.execute('INSERT INTO users(full_name, nick_name) values("園田継一郎", "そのだけいいちろう")')

conn.commit()

cur.close()
conn.close()