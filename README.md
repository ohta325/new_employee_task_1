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
2. 新しいブランチを作成し、branchを切り替える
```bash
git switch -c {社員番号}/feature
```
3. featureブランチでコードを修正する
4. 変更内容をステージングする
```bash
git add .
```
5. ステージングの内容をコミットする
```bash
git commit -m "{分かりやすいコミットメッセージ}"
```
6. リモートリポジトリにコミット内容をプッシュする
```bash
git push -u origin {社員番号}/feature
```
7. GitHub上で {社員番号}/feature → {社員番号} へのプルリクエストを作成する
8. レビュアーからコードレビューを受ける
9. レビュイーは指摘内容を修正し、4～6を行う
10. レビュアーは指摘の反映が完了していることを確認し、プルリクエストを承認する