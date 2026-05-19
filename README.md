# EU Electricity Market Analytics Platform

> A near-real-time lakehouse pipeline that ingests ENTSO-E day-ahead prices
> and load data across European bidding zones, models them dimensionally in
> Snowflake, and serves dashboards for price arbitrage and anomaly detection.

[![CI](https://github.com/AramisN/eu-electricity-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/AramisN/eu-electricity-analytics/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## The problem

> *TODO (week 1): write a 3-paragraph stakeholder story. Imagine a real
> persona — an energy trading desk, a utility, or a market regulator.
> What pain are they in today? What's broken without this system?*

Placeholder: An energy trading desk needs to track day-ahead spot prices
across all EU bidding zones, identify hourly price spreads (arbitrage
signals), and detect anomalous price spikes. Today they pull CSVs by hand
from the ENTSO-E web portal once a day, paste them into Excel, and miss
anything that happens between checks.

## Why this dataset

The ENTSO-E Transparency Platform publishes real-time and historical
electricity market data for ~35 European bidding zones. It's a genuinely
interesting data engineering problem because:

- **Time-series at scale** — hourly data × 35 zones × multiple metrics
- **Real-world quirks** — DST transitions (23- and 25-hour days), late-
  arriving corrections, bidding zone reconfigurations
- **Pan-European** — timezones, currencies, market coupling rules
- **Live stakeholders** — utilities, regulators, traders, consumers

## Architecture

> *TODO (week 1): replace this placeholder with a real diagram
> (draw.io export → docs/architecture.png, or Mermaid).*

```
[ENTSO-E API] → [Python ingestion] → [S3 + Iceberg]
                                            ↓
[Streamlit dashboard] ← [dbt marts] ← [Snowflake raw]
                              ↑
                       [Airflow orchestration]
```

## Components

| Layer | Tool | Why |
|---|---|---|
| Orchestration | Airflow 2.10 | Production-grade, what EU enterprises run |
| Ingestion | Python (httpx + pydantic) | Type-safe API client with retries |
| Lake storage | S3 + Iceberg (Glue Catalog) | Open table format, future-proof |
| Warehouse | Snowflake | EU enterprise default |
| Transformation | dbt-core (Snowflake adapter) | Standard analytics engineering |
| Presentation | Streamlit | Quickest path to a demo |
| IaC | Terraform | Reproducible infrastructure |
| CI | GitHub Actions | Lint + test on every push |

## Quickstart (local development)

> *TODO: this section gets fleshed out in week 1 once docker-compose is in place.*

Prerequisites: Python 3.11+, Docker, Terraform, an AWS account, a Snowflake trial.

```bash
# Clone and set up
git clone git@github.com:AramisN/eu-electricity-analytics.git
cd eu-electricity-analytics

# Python environment (uv recommended; venv works too)
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"

# Pre-commit hooks
pre-commit install

# Run tests
pytest
```

## Architectural decisions

All significant architectural choices are documented as
[Architecture Decision Records (ADRs)](docs/decisions/).

Notable so far:

- [ADR-000: Using ADRs](docs/decisions/000-using-adrs.md)
- [ADR-001: Snowflake as the warehouse](docs/decisions/001-snowflake-warehouse.md)

## Known limitations

- *TODO (week 4+): document real limitations as they emerge during build.*
- Placeholder: ENTSO-E API rate limit is 400 requests/minute on the
  document-level endpoints; we use bulk endpoints but throttling on
  initial backfills is still possible.

## Lessons learned

> *TODO (week 12): the most-read section of any portfolio repo.
> Filled in at end of Q1.*

## Roadmap

- **Week 1–4 (Foundation, Jun 2026)** — repo scaffolding, docker-compose
  Airflow, first ENTSO-E ingestion DAG.
- **Week 5–8 (Build, Jul 2026)** — full medallion layer in Snowflake,
  dbt models, Streamlit dashboard.
- **Week 9–12 (Polish, Aug 2026)** — production-shape it, write the case
  study, publish.

## License

[MIT](LICENSE) — feel free to learn from this. If you build on it for
client work, a star or a credit is appreciated but not required.

## About

Built by [Aramis Nasirianfar](https://www.linkedin.com/in/aramisn/) /
Aramis Software Solutions — a Finnish data engineering consultancy
specialising in lakehouse migrations and AI-data plumbing.
