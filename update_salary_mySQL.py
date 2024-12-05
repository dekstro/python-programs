import pymysql
conn=pymysql.connect(host='localhost',database='practice',user='root',password='root')
cursor=conn.cursor()
cursor.execute('update employee set salary=salary+1000 where emp_id=68319')
conn.commit()
cursor.close()
conn.close()
