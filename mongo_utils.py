from pymongo import MongoClient
from config import MONGO_URI

def run_mongo_query(query_str):
    client = MongoClient(MONGO_URI)
    db = client.chatdb
    try:
        # ⚠️ 注意：这里 query_str 应该是完整的 eval-able 语句，如：db.collection.find(...)
        return list(eval(query_str))
    except Exception as e:
        return [f"❌ Eval failed: {e}"]