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
# {社員番号}のブランチから、更にfeatureブランチを切り、featureブランチに切り替える
git switch -c feature
# featureブランチにいることを確認
git branch
```
4. 概要に記載の機能を実現するために、main.pyを修正していく
5. 変更内容をステージングする
```bash
git add .
```
6. ステージングした内容をコミットする
```bash
git commit -m "{分かりやすいコミットメッセージ}"
```
7. リモートリポジトリに、{社員番号}/featureブランチをプッシュする
```bash
git push -u origin {社員番号}/feature
```
8. GitHub上で {社員番号}/feature → {社員番号} へのプルリクエストを作成する
9. レビュアーからコードレビューを受ける
10. レビュイーは指摘内容を修正し、5～7を行う
11. レビュアーは指摘の反映が完了していることを確認し、プルリクエストを承認する
12. てすと