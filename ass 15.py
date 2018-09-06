#Q.1

import sqlite3
try:
    con=sqlite3.connect('Students.db')
    print(con)
except sqlite3.DatabaseError as e:
    if con:
        print('There is a probem') 
finally:
    con.close()
    print('no problem,DATABASE created')

#Q.2
    a=[]
for i in range(1,11):
    a.append((input('Name is:'),int(input('Marks are:'))))

#Q.3
import sqlite3
try:
    con=sqlite3.connect('Students.db')
    cursor=con.cursor()
    query='create table Students(name varchar(20),marks number(3) check (marks>=0 and marks<=100))'
    cursor.execute(query)
    print('Your table is created')
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem')
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('It is completed!')
                
import sqlite3
try:
    con=sqlite3.connect('Students.db')
    cursor=con.cursor()
    query='insert into Students (name,marks) values (?,?)'
    cursor.executemany(query,a)
    con.commit()
    print('Values are inserted')
    quer="select * from Students"
    cursor.execute(quer)
    data=cursor.fetchall()
    for row in data:
        print("NAME:{} , MARKS:{}" .format(row[0],row[1]))
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem')
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('It is done!')


#Q.4
import sqlite3
try:
    con=sqlite3.connect('Students.db')
    cursor=con.cursor()
    query="select * from Students where marks > 80"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        print("NAME:{} , MARKS:{}" .format(row[0],row[1]))
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print("everything is completed!")








