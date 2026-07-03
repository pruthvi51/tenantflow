"""
PySpark Clinical Encounter Ingestion Job for Tenant.
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from tenantflow.pyspark_engine.isolation import mask_patient_identifiers
from tenantflow.pyspark_engine.dq_gates import validate_and_route_quarantine

def run_ingest_job(spark: SparkSession, input_path: str, output_path: str, tenant_id: str):
    df = spark.read.option("header", "true").csv(input_path)
    valid_df, quaran_df, fail_rate = validate_and_route_quarantine(
        df, primary_key="encounter_id", required_cols=["patient_id", "start_time"]
    )
    masked_df = mask_patient_identifiers(valid_df, "patient_id")
    masked_df.write.mode("overwrite").parquet(f"{output_path}/valid")
    if quaran_df.count() > 0:
        quaran_df.write.mode("overwrite").parquet(f"{output_path}/quarantine")
    return {"tenant_id": tenant_id, "failure_rate": fail_rate}
