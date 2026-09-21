# ADR 0004: Two-Phase Quarantine Routing for Data Quality Gates

## Status: Accepted
## Context
Malformed EHR payloads frequently crashed downstream aggregation pipelines.

## Decision
Route schema non-conformant records to quarantine while allowing valid records to proceed.
