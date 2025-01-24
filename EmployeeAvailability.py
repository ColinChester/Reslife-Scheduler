import sqlite3
from datetime import datetime

class EmployeeAvailability:
    def __init__(self):
        self.connection = sqlite3.connect("first.db")
        self.cursor = self.connection.cursor
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS employee_availability (
                    availability_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    business_hours INTEGER,
                    employee_id INTEGER NOT NULL UNIQUE,
                    day_and_time TEXT NOT NULL,
                    FOREIGN KEY (employee_id) REFERENCES employee_info(employee_id),
                    FOREIGN KEY (business_hours) REFERENCES company_info(business_hours)
                );
        """)
        self.connection.commit()
        self.cursor.execute("""
                            INSERT INTO employee_availability ()""")
        lol = self.cursor.fetchone()
# Able to add availibilities by day with occurences happening weekly
# Use codes to represent day and time (0900A200P300P500P - Sunday 9am-2pm, 3pm-5pm)
# SQLite doesn't have a list/array type so store a delimited string to store codes
# On the front end user inputs DOW and time(s) unavailable, backend interprets this into code format
# When verifying codes for use in EmployeeShifts, compare to business_hours to verify code is eligible.
# Use business_hours to prevent EmployeeAvailablilty from recommeding times when business os closed