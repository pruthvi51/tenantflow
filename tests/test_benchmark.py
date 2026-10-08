from tenantflow.benchmarks.run_aqe_benchmark import run_benchmark


def test_aqe_benchmark_execution():
    res = run_benchmark()
    assert res["records_joined"] == 100000
    assert res["tenantflow_aqe_ms"] > 0
    assert res["cluster_utilization_gain_pct"] > 30.0
