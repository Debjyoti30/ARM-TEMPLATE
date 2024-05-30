import os
import sqlite3

# Vulnerable to SQL Injection
def get_user_info(user_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# Insecure use of os.system
def list_directory(directory):
    os.system(f'ls {directory}')

# Hardcoded sensitive information
API_KEY = '12345-ABCDE'

# Unused variable
unused_var = 42

# Function with a potential exception not handled properly
def divide_numbers(a, b):
    return a / b

# Function with a vulnerability (unsafe file operation)
def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

if __name__ == "__main__":
    user_info = get_user_info(1)
    print(user_info)
    list_directory("/tmp")
    print(divide_numbers(10, 2))
    print(read_file("example.txt"))
