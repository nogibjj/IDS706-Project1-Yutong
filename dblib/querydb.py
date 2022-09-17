from databricks import sql
import os

def querydb(query="SELECT * FROM default.diamonds LIMIT 3;"):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result

def query_carat_price(carat=0.23):
    if carat < 0.2 or carat > 1.27:
        print("The carat should between 0.2 to 1.27")
        query = "SELECT AVG(price) FROM default.diamonds"
    else:
        query = "SELECT AVG(price) FROM default.diamonds WHERE carat=" + str(round(carat, 2)) + ";"

    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        
        for row in result:
            print(row)

    return result
