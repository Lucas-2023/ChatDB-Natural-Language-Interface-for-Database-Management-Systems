import mysql.connector
from config import MYSQL_CONFIG

def run_sql_query(query):
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()

    try:
        cursor.execute(query)


        if query.strip().upper().startswith("SELECT"):
            results = cursor.fetchall()
        else:
            conn.commit()
            results = [(" Query executed successfully.",)]

    except Exception as e:
        results = [(f" SQL Error: {e}",)]

    cursor.close()
    conn.close()
    return results

