from pyspark.sql import SparkSession
from tenantflow.pyspark_engine.isolation import mask_patient_identifiers
from tenantflow.pyspark_engine.dq_gates import validate_and_route_quarantine

def test_mask_patient_identifiers():
    spark = SparkSession.builder.master("local[1]").appName("Test").getOrCreate()
    df = spark.createDataFrame([("p-001", "enc-101"), ("p-002", "enc-102")], ["patient_id", "encounter_id"])
    res = mask_patient_identifiers(df, "patient_id")
    cols = res.columns
    assert "patient_id_masked" in cols
    row = res.collect()[0]
    assert len(row["patient_id_masked"]) == 64

def test_dq_quarantine_routing():
    spark = SparkSession.builder.master("local[1]").appName("Test").getOrCreate()
    data = [
        ("enc-1", "p-1", "2024-01-01"),
        (None, "p-2", "2024-01-02"),
        ("enc-3", None, "2024-01-03")
    ]
    df = spark.createDataFrame(data, ["encounter_id", "patient_id", "start_time"])
    valid, quaran, fail_rate = validate_and_route_quarantine(df, "encounter_id", ["patient_id"])
    assert valid.count() == 1
    assert quaran.count() == 2
    assert fail_rate > 0.5
