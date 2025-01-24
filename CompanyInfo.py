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
        symbols = ":-"
        days = ['s', 'm', 't', 'w', 't', 'f']
        name = input('What is the name of your company? ').strip()
        hours = list(input('What are your business hours? Use a/p for AM and PM, dashes for ranges and commas to separate ranges. (Ex. Sunday 9:00a-3:25p, Monday 5:42p-8:00p) ').replace(" ", '').lower())
        for digit in range(len(hours)):
            if hours[digit] in symbols:
                pass
            elif hours[digit] in days:
                if hours[digit] == 's' and hours[digit + 1] != 'd':
                    if hours[digit + 1] == 'u':
                        translatedHours += '1'
                    else:
                        translatedHours += '7'
                elif hours[digit] == 't':
                    if hours[digit + 2] == 'e':
                        translatedHours += '3'
            else:
                translatedHours += str(days.index(hours[digit]))
        self.cursor.execute("""
                    INSERT INTO company_info (company_name, business_hours)
                        VALUES (?, ?)
                    """,
                    (name, hours))

        self.connection.commit()

        # s Tuesday Wednesday Thursday
        # t Saturday