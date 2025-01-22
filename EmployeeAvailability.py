import sqlite3
connection = sqlite3.connect("first.db")
cursor = connection.cursor()
class EmployeeAvailability:
    def __init__(self):
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS employee_availability (
                    availability_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    employee_id INTEGER NOT NULL UNIQUE,
                    monday TEXT NOT NULL,
                    tuesday TEXT NOT NULL,
                    wednesday TEXT NOT NULL,
                    thursday TEXT NOT NULL,
                    friday TEXT NOT NULL,
                    FOREIGN KEY (employee_id) REFERENCES employee_info(info_id)
                );
        """)
        connection.commit()
    
    def addAvailability(self, day):
        times = ['10-11', '11-12', '12-1', '1-2', '2-3', '3-4', '4-5']
        unavailableTimes = ''
        shifts = input('Enter the block of time(s) during which this person is unavailable seperated by commas. Ex. 9-10, 10-11 ').split(", ")
        for timesIndex in range(len(times)):
            for occupiedTimes in shifts:
                if occupiedTimes == times[timesIndex]:
                    times.pop(timesIndex)
        for i in range(len(timesIndex)):
            if i < len(timesIndex)-1:
                unavailableTimes += f'{i}, '
            else:
                unavailableTimes += i
        cursor.execute("""
                    INSERT INTO employee_availability (day, )
                    VALUES (?);
                    """,
                    (day.lower(), unavailableTimes))
        connection.commit()
        return True
    # currently debugging addAvailability, fixing the loop, and making it so user can edit per day
