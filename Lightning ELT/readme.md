# ⚡️ Lightning ELT: A Dockerized PostgreSQL-to-PostgreSQL Pipeline

This project delivers a clean and modular **ELT (Extract, Load, Transform)** pipeline using **Docker, PostgreSQL, and Python**. With just one command, it spins up a source and destination database, transfers data automatically via a Python script, and showcases a practical approach to containerized data engineering.

---

## 🚀 Project Highlights

- 🔄 **Postgres-to-Postgres Data Transfer**: Seamless data movement using `pg_dump` and `psql`.
- 🐳 **Fully Dockerized**: Spin up the entire stack in seconds using Docker Compose.
- ⚙️ **Automated ELT Orchestration**: Python script handles extraction, loading, and transformation (if needed).
- 📦 **Preloaded Test Data**: Source DB initialized via SQL script with ready-to-use test tables.
- 🔁 **Built-in Retry Logic**: Ensures the database is ready before running ELT logic.

---

## 🧰 Tech Stack

- **Python** – for scripting the ELT pipeline.
- **Docker & Docker Compose** – for environment orchestration.
- **PostgreSQL** – source and destination databases.
- **pg_dump & psql** – for exporting and importing SQL dumps.

---

## 🧪 Workflow Overview

1. **Startup with Docker Compose**
   - Launches three containers:
     - `source_postgres` (Preloaded)
     - `destination_postgres`
     - `elt_script` (Python automation)

2. **Initialization**
   - `init.sql` creates and populates tables in the source DB.

3. **ELT Script Execution**
   - Waits for source DB readiness.
   - Uses `pg_dump` to extract data.
   - Uses `psql` to load it into the destination DB.


