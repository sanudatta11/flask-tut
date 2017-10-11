import MySQLdb
db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="mysql",db="test")
cursor = db.cursor()
sql="""INSERT INTO test (id,name) VALUES (2,'Soumya2')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    print "changes in the database"
    db.commit()
except:
    # Rollback in case there is any error
    print "there is any error"
    db.rollback()
db.close()