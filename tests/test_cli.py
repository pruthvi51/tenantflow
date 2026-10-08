from click.testing import CliRunner

from tenantflow.cli import cli


def test_cli_plan():
    runner = CliRunner()
    res = runner.invoke(cli, ["plan", "--config-dir", "tenants"])
    assert res.exit_code == 0
    assert "12 tenant configurations" in res.output

def test_cli_deploy(tmp_path):
    runner = CliRunner()
    res = runner.invoke(cli, ["deploy", "--config-dir", "tenants", "--output-dags", str(tmp_path)])
    assert res.exit_code == 0
    assert "Successfully generated 12 dynamic Airflow DAGs" in res.output
