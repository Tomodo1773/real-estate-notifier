import sys
import uuid
from azure.cosmos import CosmosClient, PartitionKey, exceptions
from utils.config import get_database_config
from utils.line import notify_line

def initialize_cosmos_db():
    config = get_database_config()
    client = CosmosClient(url=config["url"], credential=config["key"])
    try:
        database = client.create_database_if_not_exists(id=config["database_name"])
        container = database.create_container_if_not_exists(
            id=config["container_name"], partition_key=PartitionKey(path="/link")
        )
        return container
    except exceptions.CosmosHttpResponseError as e:
        print(f"データベースまたはコンテナの作成に失敗しました: {e}")
        sys.exit(1)


def get_existing_properties(container):
    existing_properties = []
    try:
        for item in container.query_items(query="SELECT c.link FROM c", enable_cross_partition_query=True):
            existing_properties.append(item["link"])
    except exceptions.CosmosHttpResponseError as e:
        print(f"CosmosDBからのデータ取得に失敗しました: {e}")
    return existing_properties


def register_new_properties(container, properties):
    new_properties = [p for p in properties if p["link"] not in get_existing_properties(container)]
    if new_properties:
        try:
            for property in new_properties:
                property["id"] = uuid.uuid4().hex
                container.create_item(property)
                # 登録した物件(properties)をLINE Flex Messageで通知
                notify_line(property)
                print(f"新しい物件を登録しました: {property['name']}")
            print("全ての新しい物件をCosmosDBに登録しました。")
        except exceptions.CosmosHttpResponseError as e:
            print(f"物件の登録に失敗しました: {e}")
    else:
        print("登録する新しい物件はありません。")
