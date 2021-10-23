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

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)



c.execute("""
        INSERT INTO employees VALUES (?, ?, ?)
    """, 
    (emp_1.first, emp_1.last, emp_1.pay)
)

con.commit()

c.execute("""
        INSERT INTO employees VALUES (:first, :last, :pay)
    """, 
    {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay}
)

con.commit()

c.execute("SELECT * FROM employees WHERE last=:last COLLATE NOCASE", {'last':'DOE'})

print(c.fetchall())


con.close()