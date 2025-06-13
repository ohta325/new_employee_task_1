import sqlite3
import yaml

def main():
    db_file = 'test_database.db'

    try:
        conn = sqlite3.connect(db_file)
        # ここが重要: row_factory を sqlite3.Row に設定
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print(f"'{db_file}' に正常に接続しました。")

        table_name = "product_1"
        cursor.execute(f"SELECT * FROM {table_name} WHERE 0 = 1;")

        rows = cursor.fetchall()
        data_as_dicts = [dict(row) for row in rows]
        print(data_as_dicts)

        # if cursor.description:
        #     column_names = [description[0] for description in cursor.description]
        # else:
        #     print(f"テーブル '{table_name}' の情報が見つからないか、クエリに問題があります。")

        # print(column_names)

        # yaml_filename = "col.yaml"
        # with open(yaml_filename) as file:
        #     dict_col = yaml.safe_load(file)

        # drop_columns = dict_col["tables"]["drop"]
        # drop_columns.append("id")   # これは致し方ないので直接指定
        # print(dict_col["tables"]["drop"])

        # result_list = [item for item in column_names if item not in drop_columns]
        # print(result_list)

        # # データを取得する
        # print("\n--- テーブル 'product_1' の全データ(特定のカラムのみSELECT) ---")
        # select_columns = ",".join(result_list)
        # sql_statement = f"SELECT {select_columns} FROM product_1"
        # cursor.execute(sql_statement)
        # # fetchall() で全ての行を取得
        # rows = cursor.fetchall()
        # data_as_dicts = [dict(row) for row in rows]

        # print(data_as_dicts)


        # # データを取得する
        # print("\n--- テーブル 'product_1' の全データ ---")
        # cursor.execute("SELECT * FROM product_1")
        # # fetchall() で全ての行を取得
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row)

        # print("\n--- テーブル 'product_2' の全データ ---")
        # cursor.execute("SELECT * FROM product_2")
        # # fetchall() で全ての行を取得
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row)

        # print("\n--- テーブル 'master' の全データ ---")
        # cursor.execute("SELECT * FROM master")
        # # fetchall() で全ての行を取得
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row)

        # print("\n--- product_cdが'productE'のデータ ---")
        # cursor.execute("SELECT product_cd, count FROM product_1 WHERE product_cd = ?", ('productE',)) # パラメータはタプルで渡す
        # filtered_products = cursor.fetchall()
        # for product in filtered_products:
        #     print(product)
    
    except sqlite3.Error as e:
        print(f"データベース操作中にエラーが発生しました: {e}")

    finally:
        # 接続を閉じる
        if conn:
            conn.close()
            print(f"\n'{db_file}' への接続を閉じました。")

if __name__ == "__main__":
    main()