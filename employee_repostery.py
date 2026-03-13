import oracledb
from validation  import check_values

class EmployeeRepository:

    def insert_data(self, emp_id, full_name, salary, dept_id):
        check_values(emp_id,dept_id , salary)
        connection = oracledb.connect(user="SYS", password='123456789', dsn="localhost:1521/XEPDB1",mode=oracledb.SYSDBA)
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO employees(emp_id, full_name, salary, dept_id)
                VALUES (:1, :2, :3, :4)
            """, (emp_id, full_name, salary, dept_id))
            connection.commit()
            print(f"{full_name} inserted succesfully ")
        except oracledb.IntegrityError:
            print(f"Error: emp_id {emp_id} already exists")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    def show_all_employees(self):
        connection = oracledb.connect(user="SYS", password='123456789', dsn="localhost:1521/XEPDB1",mode=oracledb.SYSDBA)
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM employees")
            rows = cursor.fetchall()
            print("\n--- All employees ---")
            for row in rows:
                print(row)
            return rows
        finally:
            cursor.close()
            connection.close()

    def show_low_salary_descending(self):
        connection = oracledb.connect(user="SYS", password='123456789', dsn="localhost:1521/XEPDB1",mode=oracledb.SYSDBA)
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT * FROM employees
                WHERE salary < 500
                ORDER BY salary DESC
            """)
            rows = cursor.fetchall()
            print("\n--- People who salary less than 500(descending order) ---")
            for row in rows:
                print(row)
            return rows
        finally:
            cursor.close()
            connection.close()