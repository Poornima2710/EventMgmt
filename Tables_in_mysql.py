try : import pymysql as cntr
except ImportError : import mysql.connector as cntr
db = cntr.connect(host = 'localhost' , user = 'sqluser' , passwd = '12345')
cur = db.cursor()
cur.execute("create database if not exists cscproject")
cur.execute("use cscproject")
cur.execute("create table events \
            (ecode varchar(5) primary key,\
            ename varchar(50),\
            evenue varchar(15),\
            edate varchar(10),\
            etime varchar(8),\
            eduration bigint,\
            cname varchar(50))")
cur.execute("create table students\
            (sname varchar(50),\
            year bigint,\
            school varchar(50),\
            class_sec varchar(50),\
            email varchar(50),\
            mobile varchar(10) primary key,\
            loginid varchar(10),\
            loginpwd varchar(10))")
cur.execute("create table attend \
            (umobile varchar(10),\
            ecode varchar(5),\
            attend varchar(1))")
print("Database and Tables created successfully")
c = input("Press any key to continue-----> ")
cur.close()
db.close()
