# import pandas as pd
# import numpy as np
# import pyspark.pandas as ps
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("Python Spark for IDS706 Proj1")
    .config("spark.some.config.option", "some-value")
    .getOrCreate()
)

PATH_TRAIN = "data/train.csv"
df_train = spark.read.csv(PATH_TRAIN)
# df_train.show()
# df_train.printSchema()
psdf = df_train.pandas_api()
print(psdf.head(20))

# PATH_TEST = "data/test.csv"
# df_test = spark.read.csv(PATH_TEST)
# df_test.show()
# df_test.printSchema()
