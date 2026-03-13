import oracledb

def get_connection():
    return oracledb.connect(
        user="SYS",
        password="123456789",
        dsn="localhost:1521/XEPDB1",
        mode=oracledb.SYSDBA)
def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            CREATE TABLE employees(
                emp_id       INT PRIMARY KEY,
                full_name    VARCHAR2(50),
                salary       INT,
                dept_id      INT)
        """)
        connection.commit()
        print("Table created successfully")
    except Exception as e:
        if "ORA-00955" in str(e):
            print("Table already exists")
        else:
            print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()