import dlt
from pyspark.sql.functions import *

@dlt.table(
    comment="Raw orders data ingested from CSV"
)
def raw_orders():
    return spark.read.csv("/FileStore/raw/orders.csv", header=True)

@dlt.table(
    comment="Raw inventory data ingested from CSV"
)
def raw_inventory():
    return spark.read.csv("/FileStore/raw/inventory.csv", header=True)

@dlt.table(
    comment="Raw shipments data ingested from CSV"
)
def raw_shipments():
    return spark.read.csv("/FileStore/raw/shipments.csv", header=True)
