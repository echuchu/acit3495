import mysql.connector
import yaml

# Reading credentials
with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

# Establish a connection to MySQL server
db_conn = mysql.connector.connect(host=app_config["datastore"]["hostname"], 
                                  user=app_config["datastore"]["user"], 
                                  password=app_config["datastore"]["password"])

# Create a cursor object to execute SQL queries
db_cursor = db_conn.cursor()

# Create the 'events' database if it doesn't exist
db_cursor.execute("CREATE DATABASE IF NOT EXISTS video_db")

# Switch to the 'events' database
db_cursor.execute("USE video_db")

# Create the 'video_files' table
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS video_files (
        id INT NOT NULL AUTO_INCREMENT,
        filename VARCHAR(255) NOT NULL,
        filepath VARCHAR(255) NOT NULL,
        CONSTRAINT video_files_pk PRIMARY KEY (id)
    )
''')

# Commit the changes and close the connection
db_conn.commit()
db_conn.close()
