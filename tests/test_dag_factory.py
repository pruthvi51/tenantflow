from pathlib import Path
from tenantflow.config.loader import load_tenant_config, load_all_tenants
from tenantflow.dag_factory.compiler import compile_dag
from tenantflow.dag_factory.generator import generate_all_dags

def test_compile_dag_metro():
    root = Path(__file__).parent.parent
    cfg = load_tenant_config(root / "tenants/hospital_01_metro_health.yaml")
    code = compile_dag(cfg)
    assert "tenantflow_hospital_01_metro_health" in code
    assert "ENTERPRISE" in code
    assert "validate_config >> ingest_clinical >> aggregate_marts >> validate_sla" in code

def test_generate_all_12_dags(tmp_path):
    root = Path(__file__).parent.parent
    tenants = load_all_tenants(root / "tenants")
    count = generate_all_dags(tenants, tmp_path)
    assert count == 12
    assert (tmp_path / "dag_hospital_01_metro_health.py").exists()
    assert (tmp_path / "dag_hospital_12_desert_springs.py").exists()
