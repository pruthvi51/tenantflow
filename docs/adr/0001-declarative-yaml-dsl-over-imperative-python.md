# ADR 0001: Declarative YAML DSL Over Imperative Python Pipelines

## Status: Accepted
## Context
Onboarding new hospital affiliates took 3 weeks when writing custom Airflow DAGs.

## Decision
Adopt a declarative Pydantic-validated YAML DSL defining tenant tiers, SLAs, and storage isolation.

## Consequences
- Slashed onboarding time to 2 hours.
- Guaranteed schema validation at parse time.
