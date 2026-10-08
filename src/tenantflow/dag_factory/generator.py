"""
Dynamic DAG Batch Generator.
"""
from pathlib import Path

from tenantflow.config.models import TenantConfig
from tenantflow.dag_factory.compiler import compile_dag


def generate_all_dags(tenants: dict[str, TenantConfig], output_dir: Path) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for tenant_id, cfg in tenants.items():
        dag_code = compile_dag(cfg)
        (output_dir / f"dag_{tenant_id}.py").write_text(dag_code)
        count += 1
    return count
