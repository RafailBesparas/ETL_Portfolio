from etl.extract import extract_data  # Import the extract function from the extract module
from etl.transform import transform_data  # Import the transform function from the transform module
from etl.load import load_data  # Import the load function from the load module
from datetime import datetime  # Import datetime to log process completion time

# PostgreSQL connection URL - Update with your local database credentials
POSTGRES_URL = "postgresql://postgres:2552085124rR!@localhost:5432/CoinDatabase"

# Main ETL pipeline execution
if __name__ == "__main__":
    try:
        # Step 1: Extract data from CoinGecko API
        raw_data = extract_data()
        
        # Step 2: Transform the extracted data
        transformed_data = transform_data(raw_data)
        
        # Step 3: Load the transformed data into PostgreSQL
        load_data(transformed_data, POSTGRES_URL)
        
        # Log success and completion time
        print(f"ETL Process Completed at {datetime.now()}")
        
    except Exception as e:
        # Catch and print any errors encountered during the ETL process
        print(f"ETL Failed: {str(e)}")