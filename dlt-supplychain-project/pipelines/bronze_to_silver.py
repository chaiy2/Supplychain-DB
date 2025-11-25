import dlt
from pyspark.sql.functions import *

@dlt.table
def silver_orders():
    df = dlt.read("raw_orders")
    return df.withColumn("quantity", col("quantity").cast("int"))

@dlt.table
def silver_inventory():
    df = dlt.read("raw_inventory")
    return df

@dlt.table
def silver_shipments():
    df = dlt.read("raw_shipments")
    return df
