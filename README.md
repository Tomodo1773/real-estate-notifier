# Azure Functions プロジェクト

このプロジェクトは、Azure Functions を使用して不動産情報サイト「SUUMO」から新着物件情報を収集し、CosmosDB に登録するためのものです。また、新しい物件情報が登録された際には、LINE Bot を使って通知を行います。

## 機能

- 毎日20時に `suumo` 関数がトリガーされ、SUUMO サイトから新着物件情報を取得します。
- 取得した物件情報を CosmosDB に登録します。CosmosDB にすでに登録されている物件は登録されません。
- 新しい物件が登録された場合、LINE Bot を使って Flex Message で通知を行います。

## 前提条件

このプロジェクトを実行するには、以下の前提条件が必要です。

1. Python のインストール
   - Python 3.8 以上がインストールされていることを確認してください。
   - Python のインストール方法については、[公式ドキュメント](https://www.python.org/downloads/) を参照してください。

2. Azure Functions の作成
   - Azure ポータルにログインし、新しい Function App を作成してください。
   - Function App の作成方法については、[公式ドキュメント](https://docs.microsoft.com/ja-jp/azure/azure-functions/functions-create-function-app-portal) を参照してください。

3. Azure Cosmos DB の作成
   - Azure ポータルにログインし、新しい Azure Cosmos DB アカウントを作成してください。
   - API には Core (SQL) を選択してください。
   - Cosmos DB の作成方法については、[公式ドキュメント](https://docs.microsoft.com/ja-jp/azure/cosmos-db/create-cosmosdb-resources-portal) を参照してください。

4. LINE Developers アカウントの作成とチャンネルの設定
   - [LINE Developers](https://developers.line.biz/) にアクセスし、新しいアカウントを作成してください。
   - 新しいチャンネルを作成し、Messaging API を有効化してください。
   - チャンネルアクセストークン（長期）を取得し、環境変数 `LINE_CHANNEL_SECRET` に設定してください。
   - LINE Bot の設定方法については、[公式ドキュメント](https://developers.line.biz/ja/docs/messaging-api/building-bot/) を参照してください。

5. 環境変数の設定
   - `COSMOS_DB_ACCOUNT_URL`：Cosmos DB アカウントの URI
   - `COSMOS_DB_ACCOUNT_KEY`：Cosmos DB アカウントのプライマリキー
   - `LINE_CHANNEL_SECRET`：LINE Bot のチャンネルアクセストークン（長期）

以上の前提条件が満たされていることを確認した上で、プロジェクトを実行してください。

## ディレクトリ構造

```
azure-functions/
├── .funcignore
├── .vscode/
│ ├── extensions.json
│ ├── launch.json
│ ├── settings.json
│ └── tasks.json
├── functions/
│ ├── suumo.py
│ └── __init__.py
├── function_app.py
├── host.json
├── requirements.txt
├── utils/
│ ├── config.py
│ ├── database.py
│ ├── line.py
│ ├── web.py
│ └── __init__.py
```

## 主要ファイルの説明

- `functions/suumo.py`: SUUMO サイトから物件情報を取得し、CosmosDB に登録する関数が含まれています。
- `function_app.py`: Azure Functions のタイマートリガーを定義しています。毎日20時に `suumo` 関数が実行されます。
- `utils/web.py`: SUUMO サイトから物件情報を取得するための関数が含まれています。
- `utils/database.py`: CosmosDB への接続と物件情報の登録を行う関数が含まれています。
- `utils/line.py`: LINE Bot への Flex Message の送信を行う関数が含まれています。
- `utils/config.py`: 環境変数から CosmosDB の接続情報を取得する関数が含まれています。

## 実行方法

1. Azure Functions をデプロイします。
2. 必要な環境変数 (`COSMOS_DB_ACCOUNT_URL`、`COSMOS_DB_ACCOUNT_KEY`、`LINE_CHANNEL_SECRET`) を設定します。
3. 毎日20時に `suumo` 関数がトリガーされ、新着物件情報の取得と登録、LINE Bot への通知が行われます。

このプロジェクトでは、Azure Functions と CosmosDB、LINE Bot を組み合わせることで、不動産情報の自動収集と通知を実現しています。
