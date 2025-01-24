import sqlite3
from datetime import datetime

class EmployeeAvailability:
    def __init__(self):
        self.connection = sqlite3.connect("first.db")
        self.cursor = self.connection.cursor
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS employee_availability (
                    availability_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    employee_id INTEGER NOT NULL UNIQUE,
                    day_and_time TEXT NOT NULL,
                    FOREIGN KEY (employee_id) REFERENCES employee_info(info_id)
                );
        """)
        self.connection.commit()
# Able to add availibilities by day with occurences happening weekly
# Use codes to represent day and time (9A2P1 - 9am-2pm Sunday)
# SQLite doesn't have a list/array type so store a delimited string to store codes
# On the front end user inputs DOW and time(s) unavailable, backend interprets this into code format