import sqlite3

#実行はしないこと

# データベースに接続（無ければ新規作成）
conn = sqlite3.connect('airoco_data.db')

# カーソルを作成
cursor = conn.cursor()

# 必要なテーブルを作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    classroom TEXT,
    score REAL,
    date TEXT
)
''')

# コミットして変更を反映
conn.commit()

# 接続を閉じる
conn.close()
