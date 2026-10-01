# TenantFlow Operations Runbook

## 1. Onboarding a New Hospital Partner
1. Create `tenants/hospital_{id}_{name}.yaml`.
2. Execute dry-run validation: `make plan`.
3. Generate dynamic DAG: `make deploy`.
4. Verify pipeline SLA target via Control Plane API.

## 2. SLA Breach Triage
1. Check Airflow Gantt view for executor stragglers.
2. Verify PySpark AQE skew-join mitigation logs.
3. Check S3 quarantine directory for excessive malformed records.
