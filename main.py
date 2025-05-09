from openaiapi import convert_to_sql, convert_to_mongo
from mysql_utils import run_sql_query
from mongo_utils import run_mongo_query

def main():
    print(" Welcome to ChatDB CLI - Natural Language to Database Query")
    print("Type 'exit' to quit.\n")

    while True:
        nl_query = input(" Enter your natural language query: ")
        if nl_query.strip().lower() == "exit":
            print(" Goodbye!")
            break

        db_type = input("  Choose database (mysql/mongo): ").strip().lower()

        if db_type == "mysql":
            try:
                sql = convert_to_sql(nl_query)
                sql = sql.replace("```sql", "").replace("```", "").strip()
                print("\n Generated SQL:\n", sql)
                result = run_sql_query(sql)
                print("\n Query Result:")
                for row in result:
                    print(row)
            except Exception as e:
                print(" SQL Query Failed:", e)

        elif db_type == "mongo":
            try:
                mongo_query = convert_to_mongo(nl_query)
                mongo_query = mongo_query.replace("```python", "").replace("```", "").strip()
                print("\n Generated MongoDB query:\n", mongo_query)
                result = run_mongo_query(mongo_query)
                print("\n Query Result:")
                for doc in result:
                    print(doc)
            except Exception as e:
                print(" MongoDB Query Failed:", e)
        else:
            print(" Invalid input. Please enter 'mysql' or 'mongo'.")

if __name__ == "__main__":
    main()
