import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

# Define the engine with corrected connection string
engine = create_engine('mysql+pymysql://root:Krishna%4010@localhost:3306/practice')

# Establish the connection and execute the SQL query
try:
    connection = engine.connect()
    query = 'SELECT * FROM Employees'
    df_target = pd.read_sql(query, connection)
    print(df_target)  # Display the DataFrame with SQL data

finally:
    # Close the connection after fetching the data
    connection.close()
