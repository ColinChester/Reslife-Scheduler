import sqlite3

class EmployeeAvailability:
    def __init__(self):
        self.connection = sqlite3.connect("first.db")
        self.cursor = self.connection.cursor
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS company_info (
                    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company_name TEXT NOT NULL,
                    business_hours TEXT NOT NULL,
                    FOREIGN KEY (employee_id) REFERENCES employee_info(info_id)
                );
        """)
        self.connection.commit()