import sqlite3

dbname = 'main.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# terminalで実行したSQL文と同じようにexecute()に書く
cur.execute('SELECT * FROM users')

# 中身を全て取得するfetchall()を使って、printする。
users = cur.fetchall()


known_face_names = []
# for user_id, full_name, nick_name, status in users:
#     print(status)
for user in users:
    print(user)

cur.close()
conn.close()