# 🛣️ Toll Data ETL Pipeline with Apache Airflow

This project demonstrates an **ETL pipeline** built using **Apache Airflow** and **BashOperators**. The pipeline automates the process of unzipping, extracting, consolidating, and transforming raw toll booth data. The goal is to create a clean, analysis-ready dataset from multiple data formats.

---

# 📌 Use Case
This project simulates a real-world data engineering task for a toll system, where raw data from different formats needs to be combined and prepared for analytics or reporting.


## 📁 Files

### 🧩 `dagfile.py`
This file defines the **Apache Airflow DAG** (`ETL_toll_data`) that orchestrates the entire data pipeline.

#### 🔄 Workflow Summary:
1. **Unzip Data**  
   Extracts the archive `tolldata.tgz` to a working directory.

2. **Extract CSV Data**  
   Pulls selected fields (Row ID, Timestamp, Vehicle Number, Vehicle Type) from `vehicle-data.csv`.

3. **Extract TSV Data**  
   Pulls selected fields (Number of Axles, Toll Plaza ID, Toll Plaza Code) from `tollplaza-data.tsv`.

4. **Extract Fixed-Width Text Data**  
   Extracts fields (Payment Code and Vehicle Code) from `payment-data.txt`.

5. **Consolidate Data**  
   Merges the outputs of all three extract operations into a single CSV: `extracted_data.csv`.

6. **Transform Data**  
   Converts all text in `extracted_data.csv` to uppercase to normalize vehicle types and other string fields, producing `transformed_data.csv`.

#### ⚙️ Technology Used:
- **Apache Airflow**
- **BashOperator**
- UNIX commands: `cut`, `paste`, `tr`, `tar`

---

### 📦 `tolldata.tgz`
A compressed archive that contains the raw input data files:
- `vehicle-data.csv` – Vehicle information
- `tollplaza-data.tsv` – Toll booth metadata
- `payment-data.txt` – Fixed-width formatted payment records

These files serve as the input for the ETL pipeline defined in the DAG.

---

## 🧪 How to Use

### 1. Start Apache Airflow
```bash
airflow webserver --port 8080
airflow scheduler


# 🛣️ Toll Data ETL Pipeline with Apache Airflow

This project demonstrates an **ETL pipeline** built using **Apache Airflow** and **BashOperators**. The pipeline automates the process of unzipping, extracting, consolidating, and transforming raw toll booth data. The goal is to create a clean, analysis-ready dataset from multiple data formats.

---

## 📁 Files

### 🧩 `dagfile.py`
This file defines the **Apache Airflow DAG** (`ETL_toll_data`) that orchestrates the entire data pipeline.

#### 🔄 Workflow Summary:
1. **Unzip Data**  
   Extracts the archive `tolldata.tgz` to a working directory.

2. **Extract CSV Data**  
   Pulls selected fields (Row ID, Timestamp, Vehicle Number, Vehicle Type) from `vehicle-data.csv`.

3. **Extract TSV Data**  
   Pulls selected fields (Number of Axles, Toll Plaza ID, Toll Plaza Code) from `tollplaza-data.tsv`.

4. **Extract Fixed-Width Text Data**  
   Extracts fields (Payment Code and Vehicle Code) from `payment-data.txt`.

5. **Consolidate Data**  
   Merges the outputs of all three extract operations into a single CSV: `extracted_data.csv`.

6. **Transform Data**  
   Converts all text in `extracted_data.csv` to uppercase to normalize vehicle types and other string fields, producing `transformed_data.csv`.

#### ⚙️ Technology Used:
- **Apache Airflow**
- **BashOperator**
- UNIX commands: `cut`, `paste`, `tr`, `tar`

---

### 📦 `tolldata.tgz`
A compressed archive that contains the raw input data files:
- `vehicle-data.csv` – Vehicle information
- `tollplaza-data.tsv` – Toll booth metadata
- `payment-data.txt` – Fixed-width formatted payment records

These files serve as the input for the ETL pipeline defined in the DAG.

---

## 🧪 How to Use

### 1. Start Apache Airflow
```bash
airflow webserver --port 8080
airflow scheduler

## 3. Trigger the DAG
- Go to the Airflow UI (http://localhost:8080) and trigger the ETL_toll_data DAG manually or let it run on schedule.

