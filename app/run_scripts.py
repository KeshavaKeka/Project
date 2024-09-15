import pymysql
import subprocess
import os

# Database connection parameters
db_config = {
    'host': 'db',  # Name of the database service in docker-compose
    'user': 'root',
    'password': 'phunsukwangdoo',
    'database': 'trafficfine'
}

# List of files to execute in order (SQL and Python)
files_to_execute = [
    './sql/1.Traffic_fine_Database.sql',
    './sql/2.Create_roles.sql',
    './app/3.Insert.py',
    './sql/4.Insert_Zone_Details.sql',
    './sql/5.Insert_Foreign_Keys.sql',
    './sql/6.Create_Triggers.sql',
    './sql/7.Procedure.sql',
    './sql/8.Function.sql'
]

# Function to execute SQL files
def execute_sql_file(cursor, sql_file):
    with open(sql_file, 'r') as file:
        sql = file.read()
        cursor.execute(sql)

# Main execution
if __name__ == "__main__":
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            for file_path in files_to_execute:
                if file_path.endswith('.sql'):
                    print(f"Executing SQL file: {file_path}")
                    execute_sql_file(cursor, file_path)
                elif file_path.endswith('.py'):
                    print(f"Executing Python script: {file_path}")
                    subprocess.run(['python', file_path], check=True)
        connection.commit()
    finally:
        connection.close()