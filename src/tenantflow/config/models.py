"""
Pydantic v2 Models for TenantFlow Declarative DSL.
"""
from enum import Enum

from pydantic import BaseModel, Field


class TenantTier(str, Enum):
    ENTERPRISE = "ENTERPRISE"
    STANDARD = "STANDARD"
    LITE = "LITE"

class ResourceConfig(BaseModel):
    executor_cores: int = Field(default=4, ge=1, le=32)
    executor_memory_gb: int = Field(default=8, ge=2, le=128)
    executor_instances: int = Field(default=4, ge=1, le=64)
    shuffle_partitions: int = Field(default=32, ge=2, le=512)
    aqe_enabled: bool = True

class IsolationPolicy(BaseModel):
    storage_prefix: str
    phi_masking: str = "STRICT_SALTED_SHA256"
    date_jitter_days: int = 14

class DQGatesConfig(BaseModel):
    null_threshold_pct: float = Field(default=0.01, ge=0.0, le=1.0)
    quarantine_enabled: bool = True
    quarantine_prefix: str

class TenantConfig(BaseModel):
    tenant_id: str
    name: str
    tier: TenantTier
    sla_target_minutes: int = Field(ge=5, le=1440)
    daily_record_volume: int = Field(ge=1000)
    resource_config: ResourceConfig
    isolation_policy: IsolationPolicy
    dq_gates: DQGatesConfig
