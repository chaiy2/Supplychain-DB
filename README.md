# Delta Live Tables Supply Chain Analytics Pipeline

This project demonstrates a complete end-to-end ELT workflow implemented using
Databricks Delta Live Tables (DLT). It simulates a supply-chain dataset including
orders, inventory, and shipments, processed through a medallion architecture.

## Layers
- RAW: CSV files uploaded to /FileStore/raw
- BRONZE: Initial ingestion
- SILVER: Cleansed and typed data
- GOLD: Final business KPIs for analytics

## Technology Stack
- Databricks Community Edition
- Delta Live Tables
- PySpark
- Databricks Jobs (Workflow JSON)

## Steps to Deploy
1. Upload CSV files to /FileStore/raw
2. Create three DLT pipelines using provided Python modules
3. Upload workflow JSON to the Jobs UI
4. Run the pipeline end-to-end

## Output
- Gold table: gold_order_fulfillment
- Ready for BI dashboards and analytics
