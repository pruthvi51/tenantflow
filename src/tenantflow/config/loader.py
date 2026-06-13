"""
YAML Config Loader and Validator for TenantFlow.
"""
import yaml
from pathlib import Path
from typing import List, Dict
from tenantflow.config.models import TenantConfig

def load_tenant_config(yaml_path: Path) -> TenantConfig:
    content = yaml_path.read_text()
    data = yaml.safe_load(content)
    return TenantConfig(**data)

def load_all_tenants(config_dir: Path) -> Dict[str, TenantConfig]:
    tenants = {}
    for p in sorted(config_dir.glob("*.yaml")):
        cfg = load_tenant_config(p)
        tenants[cfg.tenant_id] = cfg
    return tenants
