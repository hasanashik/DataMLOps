import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="admin",
    password="admin",
    database="test"
)

# Create a cursor object
cursor = conn.cursor()

# Create table
create_table_query = """
CREATE TABLE IF NOT EXISTS datamlops_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT
)
"""
cursor.execute(create_table_query)
print("Table created successfully")

# Insert data into the table
insert_query = """
INSERT INTO datamlops_table (name, age)
VALUES (%s, %s)
"""
data = [
    ("John", 30),
    ("Alice", 25),
    ("Bob", 35)
]
cursor.executemany(insert_query, data)
conn.commit()
print(cursor.rowcount, "record(s) inserted successfully")

# Close cursor and connection
cursor.close()
conn.close()
