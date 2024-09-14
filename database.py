import pymysql
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path('templates') / 'info.env'
load_dotenv(dotenv_path=env_path)

def get_db_connection():
    timeout = 15
    return pymysql.connect(
        charset=os.getenv('DB_CHARSET'),
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        password=os.getenv('DB_PASSWORD'),
        read_timeout=timeout,
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        write_timeout=timeout,
    )
