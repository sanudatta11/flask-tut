import MySQLdb

def connect_mysql():
    db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="mysql",db="test")
    cursor = db.cursor()
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