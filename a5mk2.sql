-- ３．col.yamlファイルを読み込んでrequiredに定義しているカラムがNoneの行をログに出力
SELECT *
FROM
    product_1 as p1
WHERE
    (p1.product_cd or p1.flg) is null

SELECT
    p2.id,
    p2.date,
    p2.product_cd,
    p2.price,
    p2.count,
    p2.factory_cd,
    p2.flg,
    p2.test,
    p2.dummy
FROM
    product_2 as p2
WHERE
    --(p2.product_cd or p2.flg) is null
    p2.product_cd is null or p2.flg is null
    

-- ３．col.yamlファイルのrequiredに定義しているカラムがNoneの行をレコードから除外したデータ
SELECT * FROM product_1 WHERE (product_cd or flg) is not null

SELECT * FROM product_2 WHERE (product_cd or flg) is not null


-- ４．col.yamlファイルのdropに定義しているカラムを除外
-- yamlファイルの drop に定義されている'test'と'dummy'を除外したデータ
SELECT
    p1.id,
    p1.date,
    p1.product_cd,
    p1.price,
    p1.count,
    p1.factory_cd,
    p1.flg
    FROM product_1 AS p1
    WHERE (product_cd or flg) is not null
    
SELECT
    p2.id,
    p2.date,
    p2.product_cd,
    p2.price,
    p2.count,
    p2.factory_cd,
    p2.flg
    FROM product_2 AS p2
    WHERE (product_cd or flg) is not null

-- yamlファイルの drop に定義されている'test'と'dummy'を除外したデータ
SELECT
    p1.id,
    p1.date,
    p1.product_cd,
    p1.price,
    p1.count,
    p1.factory_cd,
    p1.flg
FROM product_1 AS p1
WHERE (p1.product_cd or p1.flg) is not null

SELECT
    p2.id,
    p2.date,
    p2.product_cd,
    p2.price,
    p2.count,
    p2.factory_cd,
    p2.flg
FROM product_2 AS p2

-- ５．priceとcountを乗算したuriage項目を追加
SELECT
    p1.id,
    p1.product_cd,
    p1.price * p1.count AS uriage
FROM product_1 AS p1

SELECT
    p2.id,
    p2.product_cd,
    p2.price * p2.count AS uriage
FROM product_2 AS p2
WHERE (product_cd or flg) is not null


SELECT
    product_cd,
    price * count AS uriage
FROM product_1
WHERE product_cd IS NOT NULL
GROUP BY product_cd
ORDER BY uriage desc

SELECT * 
FROM product_1 AS p1 left outer join master AS m
ON p1.factory_cd = m.factory_cd




-- 2025-06-13(fri) ----------------------------------------------------------------------------
-- product_1のカラムを取得
select *
from product_1
where 0=1

required_columns = ['product_cd', 'flg'] 
-- 各カラムに対して 'IS NULL' を適用し、リストに格納
null_conditions = [f"{column} IS NULL" for column in required_columns]
-- ' OR ' で結合して最終的な文字列を生成
sql_where_clause = " OR ".join(null_conditions)
print(sql_where_clause)

select id, date, product_cd, price, count, factory_cd, flg
from product_1
union all
select id, date, product_cd, price, count, factory_cd, flg
from product_2

-- 2025-06-16(mon)------------------------------------------------------------------------------
-- product_cdの一意な値を取得
select distinct product_cd
from product_1

-- date, product_cdでソート
select *
from product_1
order by date, product_cd






