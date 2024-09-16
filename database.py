import mysql.connector as c
import pathlib, os
from dotenv import load_dotenv

# Load environment variables from the specified .env file
env_path = pathlib.Path('templates') / 'info2.env'
load_dotenv(dotenv_path=env_path)

def get_db_connection():
    # Establish a connection to the MySQL database using environment variables
    connection = c.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASS'),
        database=os.getenv('DB_NAME')
    )
    return connection

def load_jobs_from_db():
    # Connect to the database
    connection = get_db_connection()
    
    # Use a cursor that returns rows as dictionaries
    cursor = connection.cursor(dictionary=True)
    
    # Execute a query to fetch all data from the 'jobs' table
    cursor.execute('SELECT * FROM jobs')
    
    # Fetch all the result rows as a list of dictionaries
    jobs = cursor.fetchall()
    
    # Close the cursor and connection
    cursor.close()
    connection.close()
    
    return jobs

# Example usage (can be removed when used in a web app)
jobs = load_jobs_from_db()


    
