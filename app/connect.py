import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="mysql",db="test")
cursor = db.cursor()


def insert_mysql():
    sql="""INSERT INTO test (id,name) VALUES (4,'Soumya4')"""
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        flag =  1
        db.commit()
    except:
        # Rollback in case there is any error
        flag =  0
        db.rollback()
    db.close()
    return flag

def get_data():
    sql = "SELECT * FROM test"
    list1 = []
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        for line1,line2 in data:
            l1 = []
            l1.append(line1)
            l1.append(line2)
            list1.append(l1)
        flag = 1
    except:
        flag = 0 
    return list1