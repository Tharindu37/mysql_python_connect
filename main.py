import mysql.connector

# Using mysql-connector-python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="db3"
)

# Using mysql-connector-python
cursor = conn.cursor()


# Using mysql-connector-python or PyMySQL
cursor.execute("SELECT * FROM posts")

# Fetch all rows
rows = cursor.fetchall()
for row in rows:
    print(row)


# Close the cursor
cursor.close()

# Close the connection
conn.close()