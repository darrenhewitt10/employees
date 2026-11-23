---
name: python-data-stack
description: "Project conventions for Python data work: Python 3.12+, Polars, Parquet, DuckDB, UTC timestamps, pinned dependencies and data layout. Use when writing research or pipeline code."
user-invocable: false
---
# Python data stack

## Stack
- Python 3.12+, dependency management with `uv` (or Poetry), versions pinned in a lockfile.
- **Polars** for dataframes (pandas only where a library requires it); **Parquet** storage; **DuckDB** for SQL over Parquet; Postgres only for the order/fill ledger.
- LightGBM / scikit-learn for ML; `exchange_calendars` or `pandas_market_calendars` for sessions.

## Data layout (outside git)
```
data/raw/<vendor>/<dataset>/<yyyy-mm-dd>/   # immutable downloads
data/clean/<dataset>/                        # validated, adjusted
data/features/<feature_set_version>/         # model inputs
data/llm_cache/<model>/<prompt_version>/     # cached LLM outputs
```
Partition Parquet by dataset/symbol/date. Commit schemas and code, never data.

## Conventions
- All timestamps **UTC**, timezone-aware; convert to exchange time only for display/calendar logic.
- Pure functions for transforms; no hidden global state; deterministic seeds.
- Lazy Polars queries for large scans; avoid row-wise Python loops.
- Every pipeline step is idempotent and re-runnable for a date range.
- Type hints and docstrings on public functions; tests with small fixture datasets.
