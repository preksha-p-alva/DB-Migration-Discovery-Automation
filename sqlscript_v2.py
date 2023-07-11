# Saves the output to output.txt file

import mysql.connector

# Connection details
server = '<IP-address>' # Public IP of the VM
username = '<username>' # New user and password created in Step 5.5
password = '<password>'

# Establish connection
conn = mysql.connector.connect(
    host=server,
    user=username,
    password=password
)

output_file = open("output.txt", "w")
while True:
    # Prompt user for options
    print("\n Options:")
    print("1) General queries")
    print("2) Database specific")
    print("3) Exit")
    option = input("Select an option (1, 2, or 3): ")

    if option == '1': # General queries
        query_labels_0 = [
            (f"SELECT VERSION();", "DB Version"),
            (f"SELECT COUNT(schema_name) FROM information_schema.schemata;", "Number of Databases in a given server"),
            (f"SELECT SUM(ROUND((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024)) FROM information_schema.TABLES ORDER BY (DATA_LENGTH + INDEX_LENGTH) DESC;", "Cumulative Table Size")
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
        # Execute and save all the queries
        output_file.write("\n")
        for query, label in query_labels_0:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            output_file.write(f"{label}: {rows[0][0]}\n")
        for query, label in query_labels_1:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            output_file.write(f"{label}: {rows[:][:]}\n")
        for query, label in query_labels_2:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            output_file.write(f"{label}: {rows[0][1]}\n")
            cursor.close()

    elif option == '2': # Database specific queries
        output_file.write("\n")
        database_name = input("Enter the database name: ") # Database name (classicmodels)
        query_labels = [
            (f"SELECT DISTINCT ENGINE FROM information_schema.TABLES WHERE TABLE_SCHEMA = '{database_name}';", "DB Engine"),
            (f"SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '{database_name}';", "Total tables in DB"),
            (f"SELECT SUM(ROUND((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024)) FROM information_schema.TABLES WHERE TABLE_SCHEMA = '{database_name}' ORDER BY (DATA_LENGTH + INDEX_LENGTH) DESC;","Size of all tables in MB")
        ]
        # Execute and save all the queries
        for query, label in query_labels:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            output_file.write(f"{label}: {rows[0][0]}\n")
            cursor.close()

    elif option == '3': # Exit
        break

# Close the connection
conn.close()

# Close the output file
output_file.close()
