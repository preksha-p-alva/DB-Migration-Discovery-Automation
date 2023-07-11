# DB Migration Discovery Automation

This is a simple Python script that connects to a MySQL server and allows you to execute and save the results of different queries. The script provides the following options:
1. General queries: Executes a set of general queries such as retrieving the database version, the number of databases in the server, and the cumulative table size.
2. Database-specific queries: Executes queries specific to a chosen database, including retrieving the database engine, the total number of tables, and the size of all tables.
3. Exit: Exits the program.

## Prerequisites
Before running the script, ensure that you have the following:
1. Python installed on your system.
2. The `mysql-connector-python` library installed. You can install it using the command `pip install mysql-connector-python`.

## Configuration
To configure the connection details to your MySQL server, modify the following variables in the script:
- `server`: The public IP address of the MySQL server.
- `username`: The username to authenticate with the MySQL server.
- `password`: The password to authenticate with the MySQL server.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using the command `python sqlscript.py`.
4. Follow the on-screen prompts and enter the desired options.
5. The output of the queries will be displayed on the terminal and saved to the "output.txt" file.
Note: Make sure the user specified in the configuration has appropriate permissions to execute the queries on the MySQL server.

## Output
The output of the queries will be displayed on the terminal (sqlscript_v1.py) as well as saved to the "output.txt" file (sqlscript_v2.py) in the same directory as the script. Each query result will be written on a new line in the file.

