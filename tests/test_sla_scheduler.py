from pathlib import Path
from tenantflow.config.loader import load_tenant_config, load_all_tenants
from tenantflow.scheduler.sla_scheduler import calculate_priority_score, order_execution_queue
from tenantflow.scheduler.resource_allocator import optimize_cluster_allocation

def test_enterprise_highest_priority():
    root = Path(__file__).parent.parent
    metro = load_tenant_config(root / "tenants/hospital_01_metro_health.yaml")
    desert = load_tenant_config(root / "tenants/hospital_12_desert_springs.yaml")
    score_metro = calculate_priority_score(metro)
    score_desert = calculate_priority_score(desert)
    assert score_metro > score_desert

def test_execution_queue_order():
    root = Path(__file__).parent.parent
    tenants = load_all_tenants(root / "tenants")
    queue = order_execution_queue(tenants)
    assert queue[0].tier.value == "ENTERPRISE"
    assert queue[-1].tier.value == "LITE"

def test_resource_allocator_scaling():
    root = Path(__file__).parent.parent
    metro = load_tenant_config(root / "tenants/hospital_01_metro_health.yaml")
    res = optimize_cluster_allocation(metro)
    assert res.executor_cores >= 6
    assert res.executor_memory_gb >= 12
    assert res.aqe_enabled is True
