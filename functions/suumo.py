from utils.web import get_properties
from utils.database import initialize_cosmos_db, register_new_properties

def research_suumo():
    try:
        properties = get_properties()
        if not properties:
            print("物件情報の取得に失敗しました。")
            return
        container = initialize_cosmos_db()
        register_new_properties(container, properties)
    except Exception as e:
        print(f"エラーが発生しました: {e}")


if __name__ == "__main__":
    research_suumo()
