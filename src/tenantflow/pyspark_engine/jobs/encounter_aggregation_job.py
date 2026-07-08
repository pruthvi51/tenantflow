"""
PySpark Analytical Aggregation Job.
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def run_aggregation_job(spark: SparkSession, input_path: str, output_path: str):
    df = spark.read.parquet(input_path)
    agg_df = df.groupBy("encounter_class").agg(
        F.count("encounter_id").alias("total_visits"),
        F.avg("total_claim_cost").alias("avg_cost")
    )
    agg_df.write.mode("overwrite").parquet(output_path)
    return agg_df.count()
