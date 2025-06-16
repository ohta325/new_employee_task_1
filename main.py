import sqlite3
import yaml
import csv
import os

def main():
    db_file = 'test_database.db'

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        print(f"'{db_file}' に正常に接続しました。")


        table_name = "product_1"
        cursor.execute(f"SELECT * FROM {table_name} WHERE 0 = 1;")

        if cursor.description:
            table_columns = [description[0] for description in cursor.description]
        else:
            print(f"テーブル '{table_name}' の情報が見つからないか、クエリに問題があります。")

        print(table_columns)

        yaml_filename = "col.yaml"
        with open(yaml_filename) as file:
            dict_col = yaml.safe_load(file)
        
        required_columns = dict_col["tables"]["required"]
        print(required_columns)

        drop_columns = dict_col["tables"]["drop"]
        print(drop_columns)

        result_columns = [item for item in table_columns if item not in drop_columns]
        print(result_columns)
 
        # SQLのSELECT句用に各カラム名をカンマ区切りで結合
        table_columns_join = ','.join(table_columns)
        drop_columns_join = ','.join(drop_columns)
        result_columns_join = ','.join(result_columns)

        # データを取得する
        print("\n--- テーブル 'product_1' の全データ ---")
        cursor.execute("SELECT * FROM product_1")
        # fetchall() で全ての行を取得
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        print("\n--- テーブル 'product_2' の全データ ---")
        cursor.execute("SELECT * FROM product_2")
        # fetchall() で全ての行を取得
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        print("\n--- 'product_1'と'product_2'を'product_1'のカラムに寄せ結合したデータ ---")
        productmix_query = f"SELECT {table_columns_join} FROM product_1 UNION ALL SELECT {table_columns_join} FROM product_2"
        print(f"実行するクエリ：{productmix_query}")
        cursor.execute(productmix_query)
        rows = cursor.fetchall()
        print(f"選択されたカラム{table_columns}") 
        for row in rows:
            print(row)


        # 各カラムに対して 'IS NULL' を適用し、リストに格納
        required_columns_null= [f"{column} IS NULL" for column in required_columns]
        # SQLのWHERE句用に各カラム名を'OR'区切りで結合
        required_columns_or = ' OR '.join(required_columns_null)

        print("\n--- テーブル'product_1''product_2'から required に null値をもつレコードを出力 ---")
        product_null = f"""SELECT {table_columns_join} FROM product_1
                            WHERE {required_columns_or}
                            UNION ALL
                            SELECT {table_columns_join} FROM product_2
                            WHERE {required_columns_or}"""
        print(f"実行するクエリ：{product_null}")
        cursor.execute(product_null)
        rows = cursor.fetchall()
        print(f"選択されたカラム{table_columns_join}")
        for row in rows:
            print(row)
        

        # 各カラムに対して 'IS NOT NULL' を適用し、リストに格納
        required_col_notnull = [f"{column} IS NOT NULL" for column in required_columns]
        # SQLのWHERE句用に各カラム名を'AND'区切りで結合
        required_columns_and = ' AND '.join(required_col_notnull)

        print("\n--- テーブル'product_1''product_2'から required に null値をもつレコードを除外したデータ ---")
        product_not_null = f"""SELECT {table_columns_join} FROM product_1
                                WHERE {required_columns_and}
                                UNION ALL
                                SELECT {table_columns_join} FROM product_2
                                WHERE {required_columns_and}"""        
        print(f"実行するクエリ：{product_not_null}")
        cursor.execute(product_not_null)
        rows = cursor.fetchall()
        print(f"選択されたカラム：{table_columns_join}")
        for row in rows:
            print(row)


        # yamlファイルのdropに定義されているカラムを除いた{result_columns}のデータを表示
        print("\n--- yamlファイルの drop に定義されている'test'と'dummy'を除外したデータ---")
        product_drop = f"""SELECT {result_columns_join} FROM product_1
                            WHERE {required_columns_and}
                            UNION ALL
                            SELECT {result_columns_join} FROM product_2
                            WHERE {required_columns_and}"""
        print(f"実行するクエリ：{product_drop}")
        cursor.execute(product_drop)
        rows = cursor.fetchall()
        print(f"選択されたカラム：{result_columns}")
        for row in rows:
            print(row)

        
        # priceとcountを乗算したuriage項目を追加して出力
        print("\n--- price と count を乗算した uriage 項目を追加 ---")
        cursor.execute(f"""SELECT {result_columns_join}, price * count AS uriage
                        FROM product_1 WHERE {required_columns_and}
                        UNION ALL
                        SELECT {result_columns_join}, price * count AS uriage
                        FROM product_2 WHERE {required_columns_and}""")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        
        # product_cdごとのuriage合計を算出して、uriageの降順に出力
        print("\n--- product_cd ごとの uriage 合計を算出して、uriage の降順に出力---")
        cursor.execute(f"""SELECT id, product_cd, price * count AS uriage
                       FROM product_1
                       WHERE product_cd IS NOT NULL
                       UNION ALL
                       SELECT id, product_cd, price * count AS uriage
                       FROM product_2
                       WHERE product_cd IS NOT NULL
                       GROUP BY product_cd
                       ORDER BY uriage DESC""")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        print("\n--- テーブル 'master' の全データ ---")
        cursor.execute("SELECT * FROM master")
        # fetchall() で全ての行を取得
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # テーブル'master'と'product_1''product_2'を factory_cd で外部結合
        print("\n--- テーブル'master'と'product_1''product_2'を factory_cd で外部結合したデータ ---")
        # SELECT句の各カラムのテーブルを明示するために各カラム名を', product.'区切りで結合
        result_columns_out = ', product.'.join(result_columns)
        cursor.execute(f"""SELECT product.{result_columns_out}, price * count AS uriage, m.factory_name
                        FROM(
                        SELECT {result_columns_join}, price * count AS uriage
                        FROM product_1 WHERE {required_columns_and}
                        UNION ALL
                        SELECT {result_columns_join}, price * count AS uriage
                        FROM product_2 WHERE {required_columns_and}
                        ) AS product LEFT OUTER JOIN master AS m
                        ON product.factory_cd = m.factory_cd
                       """)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        print("\n--- テーブル'master'と外部結合できなかった'product_1''product_2'のレコード ---")
        cursor.execute(f"""SELECT product.{result_columns_out}, price * count AS uriage, m.factory_name
                        FROM(
                        SELECT {result_columns_join}, price * count AS uriage
                        FROM product_1 WHERE {required_columns_and}
                        UNION ALL
                        SELECT {result_columns_join}, price * count AS uriage
                        FROM product_2 WHERE {required_columns_and}
                        ) AS product LEFT OUTER JOIN master AS m
                        ON product.factory_cd = m.factory_cd
                        WHERE m.factory_cd is null
                       """)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        print("\n--- テーブル'master'と外部結合できなかった'product_1''product_2'のレコードを除外したデータ ---")
        cursor.execute(f"""SELECT product.{result_columns_out}, price * count AS uriage, m.factory_name
                        FROM(
                        SELECT {result_columns_join}, price * count AS uriage
                        FROM product_1 WHERE {required_columns_and}
                        UNION ALL
                        SELECT {result_columns_join}, price * count AS uriage
                        FROM product_2 WHERE {required_columns_and}
                        ) AS product LEFT OUTER JOIN master AS m
                        ON product.factory_cd = m.factory_cd
                        WHERE m.factory_cd is not null
                       """)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        print("\n--- product_cdの一意な値 ---")
        cursor.execute(f"""SELECT distinct product.product_cd
                        FROM(
                        SELECT {result_columns_join}
                        FROM product_1 WHERE {required_columns_and}
                        UNION ALL
                        SELECT {result_columns_join}
                        FROM product_2 WHERE {required_columns_and}
                        ) AS product LEFT OUTER JOIN master AS m
                        ON product.factory_cd = m.factory_cd
                        WHERE m.factory_cd is not null
                       """)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        print("\n--- テーブル'master'と'product_1''product_2'を外部結合したデータを dateとproduct_cd でソートしたデータ ---")
        cursor.execute(f"""SELECT product.{result_columns_out}, price * count AS uriage, m.factory_name
                        FROM(
                        SELECT {result_columns_join}, price * count AS uriage
                        FROM product_1 WHERE {required_columns_and}
                        UNION ALL
                        SELECT {result_columns_join}, price * count AS uriage
                        FROM product_2 WHERE {required_columns_and}
                        ) AS product LEFT OUTER JOIN master AS m
                        ON product.factory_cd = m.factory_cd
                        WHERE m.factory_cd is not null
                        ORDER BY date, product_cd
                       """)
        rows = cursor.fetchall()
        for row in rows:
            print(row)


        print("\n--- product_cdが'productE'のデータ ---")
        cursor.execute("SELECT product_cd, count FROM product_1 WHERE product_cd = ?", ('productE',)) # パラメータはタプルで渡す
        filtered_products = cursor.fetchall()
        for product in filtered_products:
            print(product)


        print("\n--- データをCSVファイルに出力します ---")
        output_csv_file = 'new_employee_task_1.csv'
        cursor.execute(f"""SELECT product.{result_columns_out}, price * count AS uriage, m.factory_name
                        FROM(
                        SELECT {result_columns_join}, price * count AS uriage
                        FROM product_1 WHERE {required_columns_and}
                        UNION ALL
                        SELECT {result_columns_join}, price * count AS uriage
                        FROM product_2 WHERE {required_columns_and}
                        ) AS product LEFT OUTER JOIN master AS m
                        ON product.factory_cd = m.factory_cd
                        WHERE m.factory_cd is not null
                        ORDER BY date, product_cd
                       """)
        column_names = [description[0] for description in cursor.description]
        with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(column_names)
            csv_writer.writerows(cursor)
        print(f"--- テーブルのデータが'{output_csv_file}'に正常に出力されました ---")
    
    except sqlite3.Error as e:
        print(f"データベース操作中にエラーが発生しました: {e}")

    finally:
        # 接続を閉じる
        if conn:
            conn.close()
            print(f"\n'{db_file}' への接続を閉じました。")

if __name__ == "__main__":
    main()