# ADR 0002: Dynamic DAG Factory vs Manual DAG Definitions

## Status: Accepted
## Context
Managing 12 separate DAG codebases creates severe drift and maintenance overhead.

## Decision
Compile DAGs dynamically from tenant YAML specifications into isolated execution queues.
