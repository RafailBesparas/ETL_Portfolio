from sqlalchemy import create_engine  # Import SQLAlchemy to manage database connections
import pandas as pd  # Import pandas to load data into the database

# Function to load transformed data into PostgreSQL
def load_data(df, db_url, table_name='crypto_prices'):
    print("Loading data into PostgreSQL...")

    # Create SQLAlchemy engine to connect to PostgreSQL
    engine = create_engine(db_url)

    try:
        # Load data into the specified table (append mode)
        df.to_sql(table_name, con=engine, if_exists='append', index=False, method='multi')
        
        print("Data successfully loaded.")
    except Exception as e:
        # Print error if loading fails
        print(f"Failed to load data: {str(e)}")
