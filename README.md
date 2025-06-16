# Python課題
## SQLバージョン
### 概要
- SQLを使って以下を実現する
    - requiredにあるカラムに値が入っていないレコードは除外する。
    - ベースはproduct_1にあるカラムをSELECT。
    - DROPに指定してあるカラムはSELECTしない。
    - マスタとJOINする。
    - product_1とproduct_2をUNION ALLする。
### 手順
1. GitHubのリポジトリをクローンする
```bash
git clone https://github.com/ohta325/new_employee_task_1.git
```
2. DB(SQLite)を作成する
```bash
python make_test_db.py
```
3. 新しいブランチを作成し、branchを切り替える
```bash
# {社員番号}のブランチを作成し、{社員番号}のブランチに切り替える
git switch -c {社員番号}
# ブランチが{社員番号}のブランチにいることを確認
git branch
```
4. リモートリポジトリに、{社員番号}ブランチをプッシュする
```bash
git push -u origin {社員番号}
```
5. {社員番号}のブランチから、更に{社員番号}/featureブランチを切り、{社員番号}/featureブランチに切り替える
```bash
git switch -c {社員番号}/feature
# {社員番号}/featureブランチにいることを確認
git branch
```
6. 概要に記載の機能を実現するために、main.pyを修正していく
7. 変更内容をステージングする
```bash
git add .
```
8. ステージングした内容をコミットする
```bash
git commit -m "{分かりやすいコミットメッセージ}"
```
9. リモートリポジトリに、{社員番号}/featureブランチをプッシュする
```bash
git push -u origin {社員番号}/feature
```
10. GitHub上で {社員番号}/feature → {社員番号} へのプルリクエストを作成する
11. レビュアーからコードレビューを受ける
12. レビュイーは指摘内容を修正し、7～9を行う
13. レビュアーは指摘の反映が完了していることを確認し、プルリクエストを承認する