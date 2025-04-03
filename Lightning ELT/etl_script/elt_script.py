import subprocess
import time

def wait_for_postgres(host, max_retries=5, delay_seconds=5):
    """
    Wait for PostgreSQL to become available by checking if it is accepting connections.
    
    Args:
    - host: The hostname of the PostgreSQL server to connect to.
    - max_retries: The maximum number of attempts to connect to PostgreSQL.
    - delay_seconds: The time to wait between retries in seconds.

    Returns:
    - True if PostgreSQL is ready to accept connections within the retry limit.
    - False if the retry limit is reached and PostgreSQL is still not available.
    """
    retries = 0
    
    # Try connecting to PostgreSQL with retries
    while retries < max_retries:
        try:
            # Run the pg_isready command to check if PostgreSQL is accepting connections
            result = subprocess.run(
                ["pg_isready", "-h", host], check=True, capture_output=True, text=True)
            
            # If the result indicates PostgreSQL is accepting connections, return True
            if "accepting connections" in result.stdout:
                print("Successfully connected to PostgreSQL!")
                return True
        except subprocess.CalledProcessError as e:
            # If an error occurs (e.g., PostgreSQL is not ready), print the error and retry
            print(f"Error connecting to PostgreSQL: {e}")
            retries += 1
            print(f"Retrying in {delay_seconds} seconds... (Attempt {retries}/{max_retries})")
            time.sleep(delay_seconds)
    
    # If max retries are reached without success, print a message and return False
    print("Max retries reached. Exiting.")
    return False


# Ensure PostgreSQL is ready before starting the ELT process
if not wait_for_postgres(host="source_postgres"):
    exit(1)

print("Starting ELT script...")

# Configuration for the source PostgreSQL database (details for connecting)
source_config = {
    'dbname': 'source_db',  # Source database name
    'user': 'postgres',     # PostgreSQL user
    'password': 'secret',   # Password for the PostgreSQL user
    'host': 'source_postgres'  # Hostname of the source database (from docker-compose)
}

# Configuration for the destination PostgreSQL database (details for connecting)
destination_config = {
    'dbname': 'destination_db',  # Destination database name
    'user': 'postgres',          # PostgreSQL user
    'password': 'secret',        # Password for the PostgreSQL user
    'host': 'destination_postgres'  # Hostname of the destination database (from docker-compose)
}

# Command to dump the source database using pg_dump
dump_command = [
    'pg_dump',
    '-h', source_config['host'],
    '-U', source_config['user'],
    '-d', source_config['dbname'],
    '-f', 'data_dump.sql',  # Output the dump to a SQL file
    '-w'  # Prevent password prompt (password is set via PGPASSWORD environment variable)
]

# Set the PGPASSWORD environment variable to avoid password prompt for the source database
subprocess_env = dict(PGPASSWORD=source_config['password'])

# Execute the pg_dump command to create the SQL dump
subprocess.run(dump_command, env=subprocess_env, check=True)

# Command to load the dumped SQL file into the destination PostgreSQL database using psql
load_command = [
    'psql',
    '-h', destination_config['host'],
    '-U', destination_config['user'],
    '-d', destination_config['dbname'],
    '-a', '-f', 'data_dump.sql'  # Execute the SQL file on the destination database
]

# Set the PGPASSWORD environment variable for the destination database
subprocess_env = dict(PGPASSWORD=destination_config['password'])

# Execute the psql command to load the dump into the destination database
subprocess.run(load_command, env=subprocess_env, check=True)

print("Ending ELT script...")
