import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost',user='root',passwd='',database ='test')
if mycon.is_connected() == False:
    print('Error connecting server')
cursor = mycon.cursor()
cursor.execute('select * from student')
data = cursor.fetchone()
count = cursor.rowcount()
print('Total no. of rows printed so far ',count)
data = cursor.fetchone()
count = cursor.rowcount()
print('Total no. of rows printed so far ',count)
data = cursor.fetchmany(3)
count = cursor.rowcount()
print('Total no. of rows printed so far ',count)