import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost',user='root',passwd='',database ='test')
if mycon.is_connected() == False:
    print('Error connecting server')
cursor = mycon.cursor()
cursor.execute('select * from student')
data = cursor.fetchall()
count = count.rowcount
for row in data :
    print(row)
mycon.close()