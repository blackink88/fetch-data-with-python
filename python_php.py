#!/usr/bin/python
import MySQLdb
# Firstly, I will handle any exception
try:
    db = MySQLdb.connect(host="l27.0.0.1",      
                     db="blog",                  
                     user="******",               
                     passwd="*******     
                     )        
    cursor = db.cursor()
    my_string = "select * from blog"
    cursor.execute(my_string)
    for each_row in cur.fetchall():
        print (each_row)
    db.close()
except Exception as e:
    print('Error ', e) 
