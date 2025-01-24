import sqlite3

class EmployeeShifts:
    def __init__(self):
        self.connection = sqlite3.connect("first.db")
        self.cursor = self.connection.cursor
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS employeeSchedule (
                    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    employee_id INTEGER NOT NULL,
                    shift_day1 TEXT NOT NULL
                    shift_day2 TEXT NOT NULL
                    start_time1 TEXT NOT NULL
                    shift_time TEXT NOT NULL,
                    FOREIGN KEY (employee_id) REFERENCES employee_info(employee_id)
                );
        """)
        self.connection.commit()