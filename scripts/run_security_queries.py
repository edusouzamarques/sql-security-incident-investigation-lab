#!/usr/bin/env python3
"""
run_security_queries.py - Verifiable SQL Security Queries Lab
Google Cybersecurity Professional Certificate - Course 4: Linux and SQL
Author: Eduardo Souza Marques (@edusouzamarques)
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../database/organization.db")

def execute_query(title, query):
    print("\n" + "="*70)
    print(f"🔍 {title}")
    print("="*70)
    print(f"[SQL] {query}\n")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    
    # Print headers
    col_names = [desc[0] for desc in cursor.description]
    print(f"{' | '.join(col_names)}")
    print("-" * 70)
    
    for row in rows[:10]: # Print top rows
        print(" | ".join(str(val) for val in row))
    
    total = len(rows)
    print(f"\n[+] Total rows returned: {total}")
    conn.close()

if __name__ == "__main__":
    # Query 1: Failed after-hours logins
    execute_query(
        "1. Retrieve After-Hours Failed Login Attempts (> 18:00 and success = 0)",
        "SELECT * FROM log_in_attempts WHERE login_time > '18:00' AND success = 0;"
    )

    # Query 2: Specific incident dates
    execute_query(
        "2. Retrieve Login Attempts on Specific Incident Dates (2022-05-08 OR 2022-05-09)",
        "SELECT * FROM log_in_attempts WHERE login_date = '2022-05-08' OR login_date = '2022-05-09';"
    )

    # Query 3: Foreign geographic anomalies (Outside Mexico)
    execute_query(
        "3. Retrieve Login Attempts Outside of Mexico (NOT country LIKE 'MEX%')",
        "SELECT * FROM log_in_attempts WHERE NOT country LIKE 'MEX%';"
    )

    # Query 4: Targeted patch for Marketing East building
    execute_query(
        "4. Retrieve Employees in Marketing East Building (Marketing AND East%)",
        "SELECT * FROM employees WHERE department = 'Marketing' AND office LIKE 'East%';"
    )

    # Query 5: Patch rollout for Finance or Sales
    execute_query(
        "5. Retrieve Employees in Finance or Sales (Finance OR Sales)",
        "SELECT * FROM employees WHERE department = 'Finance' OR department = 'Sales';"
    )

    # Query 6: Enterprise rollout excluding IT
    execute_query(
        "6. Retrieve All Employees Not in IT (NOT department = 'Information Technology')",
        "SELECT * FROM employees WHERE NOT department = 'Information Technology';"
    )
