
import sqlite3

conn = sqlite3.connect('univ1.db')

cur = conn.cursor()

dno = int(input('Enter Deptno'))
dname = input('Enter dname')

cur.execute(f'insert into Dept values({dno},"{dname}")')

conn.commit()

cur.close()

conn.close()