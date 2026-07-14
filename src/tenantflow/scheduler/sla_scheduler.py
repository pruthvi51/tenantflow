"""
SLA-Aware Scheduler with Priority Queueing and Dynamic Deadlines.
"""
from typing import List, Dict
from tenantflow.config.models import TenantConfig

def calculate_priority_score(cfg: TenantConfig) -> float:
    """
    Priority score calculation:
    Higher score = earlier scheduling slot.
    Enterprise tier + tight SLA + high volume = highest priority.
    """
    tier_weights = {"ENTERPRISE": 100.0, "STANDARD": 50.0, "LITE": 10.0}
    weight = tier_weights.get(cfg.tier.value, 10.0)
    sla_urgency = 1000.0 / max(cfg.sla_target_minutes, 1)
    volume_factor = cfg.daily_record_volume / 100000.0
    return round(weight * 2.0 + sla_urgency + volume_factor, 2)

def order_execution_queue(tenants: Dict[str, TenantConfig]) -> List[TenantConfig]:
    return sorted(tenants.values(), key=calculate_priority_score, reverse=True)
