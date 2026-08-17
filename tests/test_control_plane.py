from fastapi.testclient import TestClient
from tenantflow.control_plane.app import app

client = TestClient(app)

def test_health():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json()["status"] == "HEALTHY"

def test_list_tenants():
    res = client.get("/api/v1/tenants")
    assert res.status_code == 200
    data = res.json()
    assert len(data) == 12

def test_cluster_metrics():
    res = client.get("/api/v1/metrics/cluster")
    assert res.status_code == 200
    data = res.json()
    assert data["cluster_utilization_improvement_pct"] > 30.0
    assert data["pipeline_reliability_pct"] > 99.0
