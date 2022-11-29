import pymysql as pym
mycon = sqltor.connect(host='localhost',user='root',passwd='',database ='test')
cursor = mycon.cursor()
cursor.execute('select*from student')
data =cursor.fetchall()
count = cursor.rowcount
for row in data :
    print(row)
mycon.close()