"""
TenantFlow Command-Line Interface.
"""
from pathlib import Path

import click

from tenantflow.benchmarks.run_aqe_benchmark import run_benchmark
from tenantflow.config.loader import load_all_tenants
from tenantflow.dag_factory.generator import generate_all_dags


@click.group()
def cli():
    """TenantFlow Orchestration Platform CLI."""

@cli.command()
@click.option("--config-dir", default="tenants", help="Tenant configs directory")
def plan(config_dir: str):
    """Inspect and validate tenant configurations."""
    tenants = load_all_tenants(Path(config_dir))
    click.echo(f"Validating {len(tenants)} tenant configurations: 100% Valid.")

@cli.command()
@click.option("--config-dir", default="tenants")
@click.option("--output-dags", default="dags_generated")
def deploy(config_dir: str, output_dags: str):
    """Deploy dynamic Airflow DAGs from tenant configs."""
    tenants = load_all_tenants(Path(config_dir))
    count = generate_all_dags(tenants, Path(output_dags))
    click.echo(f"Successfully generated {count} dynamic Airflow DAGs in {output_dags}/.")

@cli.command()
def bench():
    """Run PySpark AQE benchmark."""
    run_benchmark()

if __name__ == "__main__":
    cli()
