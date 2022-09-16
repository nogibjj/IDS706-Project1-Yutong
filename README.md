# IDS706-Project1-Yutong

## Intro
A command line tool to query data stored in databricks

## Usage

#### Test out databricks
```
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq
```

#### Use command line tool 
```
./query_db.py cli-query
./query_db.py cli-query --query=<your query statement>
```

#### Access fast api web app
```
python3 ./fastapi_app.py
```
Then open the url with the pop-up window
