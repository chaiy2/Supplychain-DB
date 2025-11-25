import dlt
from pyspark.sql.functions import *

@dlt.table(
    comment="Final business gold table for supply-chain KPIs"
)
def gold_order_fulfillment():
    orders = dlt.read("silver_orders")
    shipments = dlt.read("silver_shipments")
    inventory = dlt.read("silver_inventory")

    return (orders
            .join(shipments, "order_id", "left")
            .join(inventory, "product_id", "left")
            .select(
                "order_id",
                "product_name",
                "quantity",
                "order_date",
                "shipment_date",
                "status",
                "warehouse"
            )
            .orderBy("order_id")
    )
