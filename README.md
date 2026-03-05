# Data Pipeline Learning Repository

Learning data engineering fundamentals through hands-on implementation of containerized data pipelines.

## Why This Exists

Building foundational knowledge for **Ziddfit** - an all-in-one ecosystem for fitness enthusiasts centered around gym owners (the closest stakeholders to trainers and clients). The goal is to streamline gym operations, eliminate register-based workflows, and create value for the entire fitness community.

### The Onboarding Challenge

Indian gyms maintain member data in physical registers. Onboarding to new tech is hard because years of data exists only on paper.

### The Solution

Learn data pipelines and ingestion workflows to build:
- OCR-based data extraction from physical registers
- Automated ingestion pipelines for seamless database migration
- Frictionless onboarding so gym owners can adopt Ziddfit's platform without manual data entry

This repository is the foundation - understanding how data flows from source to database before building production pipelines for gym onboarding.

## What This Does

Data ingestion pipeline that fetches data from a URL, processes it with pandas, saves to CSV, and loads into PostgreSQL in chunks to avoid memory issues.

Working with NYC Taxi trip data (government dataset available up to 2021).

## Project Structure

```
.
├── ingest_pipe.py       # Main ingestion script (URL → pandas → CSV → PostgreSQL)
├── Dockerfile           # Containerizes ingest_pipe.py
├── pyproject.toml       # uv dependencies
└── uv.lock              # uv lock file
```

## Stack

- **PostgreSQL**: Running in Docker container locally
- **pgcli**: Terminal-based database client
- **pgAdmin**: GUI database management
- **Python**: Data processing and ingestion
- **pandas**: DataFrame operations
- **Docker**: Script containerization

## Usage

The ingestion script loads data from URL to pandas DataFrame, writes to CSV, then ingests into PostgreSQL in chunks for memory efficiency.

Database connection via pgcli in terminal or pgAdmin for GUI access.

## Timeline

**March 2026** - Started serious data science journey
- Set up PostgreSQL in Docker
- Built first data ingestion pipeline
- Learned containerization with Docker
- Implemented chunked data loading for memory efficiency