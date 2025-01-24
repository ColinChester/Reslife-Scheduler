import sqlite3
self.connection = sqlite3.connect("first.db")
self.cursor = self.connection.self.cursor()
class EmployeeSchedule:
    def __init__(self):
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS employeeSchedule (
                    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    employee_id INTEGER NOT NULL,
                    shift_day1 TEXT NOT NULL
                    shift_day2 TEXT NOT NULL
                    start_time1 TEXT NOT NULL
                    shift_time TEXT NOT NULL,
                    FOREIGN KEY (employee_id) REFERENCES employee_info(info_id)
                );
        """)
        self.connection.commit()