import oracledb
import matplotlib.pyplot as plt
class DepartmentStatistics:
    def show_statisctics(self):
        connection = oracledb.connect(user="SYS", password='123456789', dsn="localhost:1521/XEPDB1",mode=oracledb.SYSDBA)
        cursor = connection.cursor()
        try:
            cursor.execute("""
                        SELECT dept_id, MIN(salary), MAX(salary)
                        FROM employees
                        GROUP BY dept_id
                    """)
            rows = cursor.fetchall()
            print("\n--- Minimum and maximum salary for each department ---")
            for row in rows:
                print(f"Department id:{row[0]}| minimum salary:{row[1]}| maximum salary:{row[2]}")
            return rows
        finally:
            cursor.close()
            connection.close()
    def show_charts(self):
        rows=self.show_statisctics()
        departments = [row[0] for row in rows]
        min_salaries = [row[1] for row in rows]
        max_salaries = [row[2] for row in rows]
        x = range(len(departments))

        plt.figure(figsize=(10, 6))
        plt.bar([i - 0.2 for i in x], min_salaries, width=0.4, label='Min Maaş', color='red')
        plt.bar([i + 0.2 for i in x], max_salaries, width=0.4, label='Max Maaş', color='blue')


        plt.xticks(x, departments)
        plt.xlabel("Department")
        plt.ylabel("Salary")
        plt.title("Min and Max Salary for each Department")
        plt.legend()
        plt.tight_layout()
        plt.show()


