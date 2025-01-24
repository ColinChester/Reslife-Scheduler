import sqlite3

class CompanyInfo:
    def __init__(self):
        self.connection = sqlite3.connect("first.db")
        self.cursor = self.connection.cursor
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS company_info (
                    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company_name TEXT NOT NULL,
                    business_hours TEXT NOT NULL,
                );
        """)
        self.connection.commit()
        self.getInfo()
    
    def __getInfo(self):
        translatedHours = ''
        name = input('What is the name of your company? ').strip()
        hours = input('What are your business hours? Use dashes for ranges and commas to separate ranges. (Ex. 9:00am-3:25pm, 5:42pm-8:00pm) ').lower()
        self.cursor.execute("SELECT company_id FROM company_info LIMIT 1")
        self.cursor.execute("""
                    INSERT INTO company_info (company_name, business_hours)
                        VALUES (?, ?)
                    """,
                    (name, hours))

        self.connection.commit()