import mysql.connector

# Connection details
server = '<IP-address>' # PubliC IP of the VM
username = '<username>' # New user and password created
password = '<password>'
# Establish connection
conn = mysql.connector.connect(
    host=server,
    user=username,
    password=password
)

# Prompt user for options
print("Options:")
print("1) General queries")
print("2) Database specific")
option = input("Select an option (1 or 2): ")

# Execute queries based on user option
if option == '1': # General queries
    query_labels_0 = [
        (f"SELECT VERSION();", "DB Version"),
        (f"SELECT COUNT(schema_name) FROM information_schema.schemata;", "Number of Databases in a given server"),
        (f"SELECT SUM(ROUND((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024)) FROM information_schema.TABLES ORDER BY (DATA_LENGTH + INDEX_LENGTH) DESC;", "Cummilative Table Size")
    ]
    query_labels_1 = [
        (f"SELECT table_schema, SUM(data_length + index_length) FROM information_schema.tables GROUP BY table_schema;", "Size of each DB")
    ]
    query_labels_2 = [
        ("SHOW VARIABLES LIKE 'gtid_mode';", "GTID Mode"),
        ("SHOW VARIABLES LIKE 'read_only';", "Replication"),
        ("SHOW VARIABLES LIKE 'log_bin';", "Binlog status"),
        ("SHOW VARIABLES LIKE 'binlog_format';", "Binlog format"),
        ("SHOW VARIABLES LIKE 'expire_logs_days';", "Log Extension Period")
        
    ]    
    # Execute and print all the queries
    print("\n")
    for query, label in query_labels_0:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        print(f"{label}: {rows[0][0]}") 
    for query, label in query_labels_1: 
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        print(f"{label}: {rows[:][:]}")
    for query, label in query_labels_2:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        print(f"{label}: {rows[0][1]}")
        cursor.close()
    
elif option == '2': # Database specific queries
    print("\n")
    database_name = input("Enter the database name: ") # Database name (classicmodels)
    query_labels = [
        (f"SELECT DISTINCT ENGINE FROM information_schema.TABLES WHERE TABLE_SCHEMA = '{database_name}';", "DB Engine"),
        (f"SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '{database_name}';", "Total tables in DB"),
        (f"SELECT SUM(ROUND((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024)) FROM information_schema.TABLES WHERE TABLE_SCHEMA = '{database_name}' ORDER BY (DATA_LENGTH + INDEX_LENGTH) DESC;","Size of all tables in MB")
    ]
    # Execute and print all the queries
    for query, label in query_labels:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        print(f"{label}: {rows[0][0]}")
        cursor.close()

# Close the connection
conn.close()
