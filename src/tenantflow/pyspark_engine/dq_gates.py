"""
Automated Data Quality Validation Gates with Quarantine Routing.
"""
from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from typing import Tuple

def validate_and_route_quarantine(
    df: DataFrame,
    primary_key: str,
    required_cols: list[str]
) -> Tuple[DataFrame, DataFrame, float]:
    """
    Validates data quality constraints:
    - Primary key non-null and non-empty
    - Required columns non-null
    Splits into valid DataFrame and quarantine DataFrame.
    """
    condition = F.col(primary_key).isNotNull() & (F.length(F.trim(F.col(primary_key))) > 0)
    for col in required_cols:
        condition = condition & F.col(col).isNotNull()

    valid_df = df.filter(condition)
    quarantine_df = df.filter(~condition)

    total = df.count()
    quarantine_count = quarantine_df.count()
    failure_rate = (quarantine_count / total) if total > 0 else 0.0

    return valid_df, quarantine_df, failure_rate
