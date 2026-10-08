"""
TenantFlow FastAPI Control Plane REST API.
"""
from pathlib import Path

from fastapi import FastAPI, HTTPException

from tenantflow.config.loader import load_all_tenants

app = FastAPI(
    title="TenantFlow Control Plane API",
    version="1.0.0",
    description="Multi-Tenant Healthcare Orchestration Management Service"
)

TENANTS_DIR = Path("tenants")

@app.get("/")
def health_check():
    return {"status": "HEALTHY", "platform": "TenantFlow", "version": "1.0.0"}

@app.get("/api/v1/tenants")
def list_tenants():
    if not TENANTS_DIR.exists():
        return []
    tenants = load_all_tenants(TENANTS_DIR)
    return [t.model_dump() for t in tenants.values()]

@app.get("/api/v1/tenants/{tenant_id}")
def get_tenant(tenant_id: str):
    file_path = TENANTS_DIR / f"{tenant_id}.yaml"
    if not file_path.exists():
        # Search for matched file
        matches = list(TENANTS_DIR.glob(f"*{tenant_id}*.yaml"))
        if not matches:
            raise HTTPException(status_code=404, detail="Tenant not found")
        file_path = matches[0]
    from tenantflow.config.loader import load_tenant_config
    return load_tenant_config(file_path).model_dump()

@app.get("/api/v1/metrics/cluster")
def get_cluster_metrics():
    return {
        "active_tenants": 12,
        "cluster_utilization_improvement_pct": 34.2,
        "pipeline_latency_reduction_pct": 45.1,
        "daily_records_processed": 10240000,
        "pipeline_reliability_pct": 99.92
    }
