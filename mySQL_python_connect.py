import pymysql
conn=pymysql.connect(host='localhost',database='practice',user='root',password='root')
cursor=conn.cursor()
cursor.execute('select * from employee')
rows=cursor.fetchall()
for i in rows:
    print(i)
cursor.close()
conn.close()