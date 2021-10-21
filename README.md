# FiftyOne の実行例

[FiftyOne] を Python スクリプト、 Jupyter notebook で実行する例

## 実行環境

- Python 3.9.6

### Proxy 環境用の設定

環境変数に Proxy サーバーの URL を指定する

```sh
export HTTP_PROXY=http://<hostname>:<port>
export HTTPS_PROXY=http://<hostname>:<port>
```

### 依存パッケージのインストール

```sh
pip install --requirement requirements.txt
```

## スクリプトの実行

```sh
cd scripts
python list_zoo_datasets.py
```

## ノートブックの実行

```sh
cd notebooks
jupyter lab
```

## 編集方法

- Node.js をインストールする

- `npm install` を実行する

- `pre-commit install` を実行する

- ブランチを作成し、編集結果をコミットする

  pre-commit と commitlint によるチェックが行われる

- プルリクエストを作成する

  Super Linter によるチェックが行われる

[fiftyone]: https://voxel51.com/
