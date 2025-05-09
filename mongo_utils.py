from pymongo import MongoClient
from config import MONGO_URI

def run_mongo_query(query_str):
    client = MongoClient(MONGO_URI)
    db = client["movie"]

    try:
        local_vars = {"db": db}

        exec("result = " + query_str, {}, local_vars)
        result = local_vars["result"]

        if hasattr(result, "inserted_id"):
            return [f" Inserted document with _id: {result.inserted_id}"]

        elif hasattr(result, "deleted_count"):
            return [f" Deleted {result.deleted_count} document(s)"]

        elif hasattr(result, "modified_count"):
            return [f" Modified {result.modified_count} document(s)"]

        elif hasattr(result, "__iter__"):
            return list(result)

        else:
            return [str(result)]

    except Exception as e:
        return [f" MongoDB Query Failed: {e}"]

