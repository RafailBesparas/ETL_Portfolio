## 📄 File Descriptions

### 1. `Dockerfile`
The `Dockerfile` defines a custom Docker image for running the ELT process. It sets up a lightweight Python environment with the necessary tools (like `pg_dump` and `psql`) to extract data from the source PostgreSQL database and load it into the destination database. It ensures the `elt_script.py` runs in a controlled and reproducible containerized environment.

### 2. `elt_script.py`
This is the heart of the ELT pipeline. The script performs the following steps:
- Waits until the source PostgreSQL container is ready.
- Extracts data from the source database using `pg_dump`.
- Loads the extracted data into the destination database using `psql`.
It uses subprocess calls and environment variables to securely automate the data transfer process between two Dockerized PostgreSQL instances.
