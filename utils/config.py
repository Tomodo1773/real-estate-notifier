import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()


def get_database_config():
    return {
        "url": os.getenv("COSMOS_DB_ACCOUNT_URL"),
        "key": os.getenv("COSMOS_DB_ACCOUNT_KEY"),
        "database_name": "PROPERTIES",
        "container_name": "SUUMO",
    }
