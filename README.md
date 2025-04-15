# Friction Graph Maker

摩擦試験データからグラフを生成するPythonスクリプト

## インストール手順

1. リポジトリのクローン:
```bash
git clone https://github.com/ユーザー名/リポジトリ名.git
cd リポジトリ名
```

2. 仮想環境の作成と有効化:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. 必要なパッケージのインストール:
```bash
pip install -r requirements.txt
```

## 使い方

1. データファイル（.txt）を用意
2. 仮想環境を有効化:
```bash
.\venv\Scripts\activate
```
3. 以下のコマンドを実行:
```bash
python friction_graph.py データファイル.txt
```
4. グラフが`graphis`フォルダに保存されます

## 入力ファイル形式
- 22行目までヘッダー
- スペース区切りのデータ
- 必要な列:
  - 1列目: Sliding count (times)
  - 3列目: Load (Nm)
  - 4列目: Friction force (Nm)

## 必要なライブラリ
- pandas
- matplotlib

## 開発環境のセットアップ
新しい環境で開発する場合:
```bash
python -m venv venv
.\venv\Scripts\activate
pip install pandas matplotlib
pip freeze > requirements.txt
```