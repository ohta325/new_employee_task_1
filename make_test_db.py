import sqlite3
import os

def make_test_db():
    # データベースファイルのパスを定義
    # 現在のスクリプトと同じディレクトリに test_database.db という名前で作成します。
    db_file = 'test_database.db'

    # もし既にデータベースファイルが存在する場合は削除し、まっさらな状態から始める
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"既存のデータベースファイル '{db_file}' を削除しました。")

    # データベースに接続する
    # 指定したファイルが存在しない場合、自動的に作成されます。
    # 接続オブジェクト (conn) とカーソルオブジェクト (cursor) を取得します。
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        print(f"'{db_file}' に正常に接続しました。")

        # テーブルを作成する
        # DROP TABLE IF EXISTS は、もし同じ名前のテーブルが既に存在すれば削除し、新しく作成するため。
        # テスト用途で何度もスクリプトを実行する場合に便利です。

        # product_1 テーブル
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS product_1 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                product_cd TEXT,
                price INTEGER,
                count INTEGER,
                factory_cd TEXT,
                flg INTEGER,
                test TEXT,
                dummy TEXT
            )
        """)

        print("テーブル 'product_1' を作成しました。")

        # 複数のデータを挿入 (executemanyを使用)
        product_1_data = [
             ('2025/6/1','productA',100,1,'fcA',0,'test','dummy'),
             ('2025/6/1','productB',200,2,'fcA',0,'test','dummy'),
             ('2025/6/1','productC',300,3,'fcA',0,'test','dummy'),
             ('2025/6/1','productD',400,4,'fcB',0,'test','dummy'),
             ('2025/6/1','productE',500,5,'fcB',0,'test','dummy'),
             ('2025/6/2',None,100,1,'fcA',0,'test','dummy'),
             ('2025/6/2','productB',200,2,'fcA',0,'test','dummy'),
             ('2025/6/2',None,300,3,'fcA',0,'test','dummy'),
             ('2025/6/2','productE',500,4,'fcB',0,'test','dummy'),
             ('2025/6/3','productE',500,5,'fcB',0,'test','dummy'),
        ]
        cursor.executemany("INSERT INTO product_1 (date, product_cd, price, count, factory_cd, flg, test, dummy) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", product_1_data)
        print("product_1にデータを挿入しました。")

        # product_2 テーブル
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS product_2 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                product_cd TEXT,
                category TEXT,
                price INTEGER,
                count INTEGER,
                factory_cd TEXT,
                flg INTEGER,
                test TEXT,
                dummy TEXT
            )
        """)

        print("テーブル 'product_2' を作成しました。")

        product_2_data = [
             ('2025/6/3','productA','typeA',100,1,'fcC',0,'test','dummy'),
             ('2025/6/3','productB','typeA',200,2,'fcC',None,'test','dummy'),
             ('2025/6/4','productC','typeA',300,3,'fcD',None,'test','dummy'),
             ('2025/6/4','productD','typeA',400,4,'fcC',1,'test','dummy'),
             ('2025/6/5','productE','typeA',500,5,'fcA',1,'test','dummy'),
             ('2025/6/5','productA','typeA',100,1,'fcB',0,'test','dummy'),
             ('2025/6/1','productB','typeA',200,2,'fcA',0,'test','dummy'),
             ('2025/6/2','productC','typeA',300,3,'fcE',1,'test','dummy'),
             ('2025/6/3','productE','typeA',500,4,'fcB',0,'test','dummy'),
             ('2025/6/4','productE','typeB',500,5,'fcB',0,'test','dummy'),
        ]
        cursor.executemany("INSERT INTO product_2 (date, product_cd, category, price, count, factory_cd, flg, test, dummy) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", product_2_data)
        print("product_2にデータを挿入しました。")

        # master テーブル
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS master (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                factory_cd TEXT,
                factory_name TEXT
            )
        """)

        print("テーブル 'master' を作成しました。")

        master_data = [
             ('fcA','工場A'),
             ('fcB','工場B'),
             ('fcC','工場C')
        ]
        cursor.executemany("INSERT INTO master (factory_cd, factory_name) VALUES (?, ?)", master_data)
        print("masterにデータを挿入しました。")

        # 変更をコミット（データベースに保存）する
        conn.commit()
        print("変更をコミットしました。")

    except sqlite3.Error as e:
        print(f"データベース操作中にエラーが発生しました: {e}")

    finally:
        # 6. 接続を閉じる
        if conn:
            conn.close()
            print(f"\n'{db_file}' への接続を閉じました。")

if __name__ == "__main__":
    make_test_db()