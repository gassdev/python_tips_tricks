import sqlite3
from employee import Employee

con = sqlite3.connect(':memory:')
# con = sqlite3.connect('employee.db')

c = con.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        first text,
        last text,
        pay integer
    )
""")

def insert_emp(emp):
    with con:
        c.execute("""
            INSERT INTO employees VALUES (?, ?, ?)
        """, 
            (emp.first, emp.last, emp.pay)
        )

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last COLLATE NOCASE", {'last':lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with con:
        c.execute("""
            UPDATE employees SET pay=:pay
            WHERE first=:first AND last=:last
        """,
        {'pay':pay, 'first':emp.first, 'last':emp.last}
        )

def remove_emp(emp):
    with con:
        c.execute("""
        DELETE FROM employees WHERE first=:first AND last=:last
        """, {'first': emp.first, 'last': emp.last}
        )

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('doe')
print(emps)

con.close()