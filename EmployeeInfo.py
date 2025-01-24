import sqlite3
class EmployeeInfo:
    def __init__(self):
        self.connection = sqlite3.connect("first.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS employee_info (
                    info_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    bison_id CHAR(9) NOT NULL UNIQUE
                );
        """)
        self.connection.commit()

    def addEmp(self, fName, lName, email, bisonId):
        self.cursor.execute("""
                    INSERT INTO employee_info (first_name, last_name, email, bison_id)
                    VALUES (?, ?, ?, ?);
                    """,
                    (fName, lName, email, bisonId))
        self.connection.commit()
        return True

    def updateEmp(self, id, fName, lName, email, bisonId):
        self.cursor.execute("""
                    UPDATE employee_info
                    SET
                        first_name = ?,
                        last_name = ?,
                        email = ?,
                        bison_id = ?
                    WHERE id = ?;
                    """,
                    (fName, lName, email, bisonId, id))
        self.connection.commit()
        return True
    
    def deleteEmp(self, id):
        self.cursor.execute("SELECT * FROM employee_info WHERE id = ?;", (id,))
        user = self.cursor.fetchone()
        
        verification = input("Enter the first name and student ID of the person you are looking to delete, seperated by a comma. ").replace(" ", "")
        verifID, verifName = verification.split(",")[0], verification.split(",")[1]

        if verifID == user[4] and verifName == user[2]:
            self.cursor.execute("""
                        DELETE FROM employee_info
                        WHERE id = ?;
                        """,
                        (user[0],))
            self.connection.commit()
            return True
        elif verifID != user[4]:
            print('Incorrect student ID.')
        else:
            print("Incorrect name.")

    def getEmp(self):
        self.cursor.execute("SELECT * FROM employee_info")
        users = self.cursor.fetchall()
        return users

list = EmployeeInfo()
print(list.getEmp())