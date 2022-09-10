# import pandas as pd
# import numpy as np
# import pyspark.pandas as ps
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("Python Spark for IDS706 Proj1")
    .config("spark.some.config.option", "some-value")
    .getOrCreate()
)

path_train = "data/train.csv"
df_train = spark.read.csv(path_train)
df_train.show()

path_test = "data/test.csv"
df_test = spark.read.csv(path_test)
df_test.show()
