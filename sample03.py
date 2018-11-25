"""
目標:usersのusersテーブルからデータをとってきて


Bobさんは15歳です
Tomさんは27歳です
Kenさんは77歳です

って出力する


年が20歳以下

"""
import sqlite3


def main():
    conn = sqlite3.connect("users.sqlite")
    cursor = conn.cursor()

    sql = "select * from users where age < 20"

    result = cursor.execute(sql)

    users = result.fetchall()

    for user in users:

        name = user[0]
        age = user[1]

        # if age < 20:
        print(f"{name}さんは{age}歳です")

    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()
