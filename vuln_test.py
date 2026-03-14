import sqlite3
import os

# Hardcoded credentials - security issue
DB_PASSWORD = "admin123"
API_KEY = "sk-prod-abc123secretkey9999"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def get_user(user_input):
    conn = sqlite3.connect("users.db")
    # SQL injection vulnerability
    query = "SELECT * FROM users WHERE id = " + user_input
    return conn.execute(query)

def run_command(cmd):
    # Command injection
    os.system("ls " + cmd)

def evaluate(expr):
    # Arbitrary code execution
    return eval(expr)
