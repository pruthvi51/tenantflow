.PHONY: help setup plan deploy test demo bench paper clean

help:
	@echo "TenantFlow Orchestration Platform Commands:"
	@echo "  make setup     Install dependencies with uv"
	@echo "  make plan      Run dry-run plan on tenant configurations"
	@echo "  make deploy    Deploy dynamic Airflow DAGs from configs"
	@echo "  make test      Execute unit and pipeline test suite"
	@echo "  make demo      Launch Streamlit tenant control console"
	@echo "  make bench     Run PySpark AQE & distributed DQ benchmark"
	@echo "  make paper     Compile LaTeX technical paper with tectonic"

setup:
	uv pip install -e ".[dev]"

plan:
	python3 -m tenantflow.cli plan --config-dir tenants/

deploy:
	python3 -m tenantflow.cli deploy --config-dir tenants/ --output-dags dags_generated/

test:
	pytest -v tests/

demo:
	streamlit run ui/app.py

bench:
	python3 -m tenantflow.benchmarks.run_aqe_benchmark

paper:
	cd paper && tectonic tenantflow_architecture_paper.tex

clean:
	rm -rf dags_generated/ .pytest_cache logs/ target/
