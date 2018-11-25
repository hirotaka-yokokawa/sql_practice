import sqlite3

"""
目標:PythonでSQLを使ってテーブルをつくる

"""


def main():
    # DB接続
    conn = sqlite3.connect("users.sqlite")
    cursor = conn.cursor()

    # SQLの準備
    sql = """CREATE TABLE users (
                name TEXT,
                age INTEGER
                )"""

    # SQLの準備
    cursor.execute(sql)

    # コミット
    conn.commit()

    ##SQLの準備
    conn.close()


if __name__ == "__main__":
    main()
