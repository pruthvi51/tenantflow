"""
TenantFlow SparkSession Factory with Dynamic Adaptive Query Execution (AQE).
"""
from pyspark.sql import SparkSession

from tenantflow.config.models import TenantConfig


def get_spark_session(tenant_cfg: TenantConfig) -> SparkSession:
    res = tenant_cfg.resource_config
    builder = (
        SparkSession.builder
        .appName(f"TenantFlow-{tenant_cfg.tenant_id}")
        .master("local[2]")
        .config("spark.sql.adaptive.enabled", str(res.aqe_enabled).lower())
        .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
        .config("spark.sql.adaptive.skewJoin.enabled", "true")
        .config("spark.sql.shuffle.partitions", str(res.shuffle_partitions))
    )
    return builder.getOrCreate()
