from pathlib import Path
from tenantflow.config.loader import load_tenant_config, load_all_tenants
from tenantflow.config.models import TenantTier

def test_load_enterprise_tenant():
    root = Path(__file__).parent.parent
    cfg = load_tenant_config(root / "tenants/hospital_01_metro_health.yaml")
    assert cfg.tenant_id == "hospital_01_metro_health"
    assert cfg.tier == TenantTier.ENTERPRISE
    assert cfg.sla_target_minutes == 15
    assert cfg.resource_config.executor_cores == 8
    assert cfg.resource_config.aqe_enabled is True

def test_load_all_12_tenants():
    root = Path(__file__).parent.parent
    tenants = load_all_tenants(root / "tenants")
    assert len(tenants) == 12
    assert "hospital_01_metro_health" in tenants
    assert "hospital_12_desert_springs" in tenants
