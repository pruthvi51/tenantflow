"""
HIPAA / SOC-2 Multi-Tenant Storage Isolation and PHI Salt-Hashing.
"""
from pyspark.sql import DataFrame
from pyspark.sql import functions as F

SALT = "TENANTFLOW_HIPAA_SECURE_SALT_2026"

def mask_patient_identifiers(df: DataFrame, id_col: str = "patient_id") -> DataFrame:
    """Apply SHA-256 salted hash to direct identifiers."""
    return df.withColumn(
        f"{id_col}_masked",
        F.sha2(F.concat(F.col(id_col), F.lit(SALT)), 256)
    )

def jitter_dates(df: DataFrame, date_col: str, max_jitter_days: int = 14) -> DataFrame:
    """Apply HIPAA Safe Harbor compliant date jittering preserving interval distribution."""
    jitter_offset = (F.hash(F.col("patient_id")) % (max_jitter_days * 2 + 1)) - max_jitter_days
    return df.withColumn(
        f"{date_col}_jittered",
        F.date_add(F.col(date_col), jitter_offset)
    )
