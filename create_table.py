import sqlite3

dbname = 'main.db'
conn = sqlite3.connect(dbname)
# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

cur.execute('CREATE TABLE users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, full_name STRING, nick_name STRING, status BOOLEAN)')

# データベースへコミット。これで変更が反映される。
conn.commit()
conn.close()