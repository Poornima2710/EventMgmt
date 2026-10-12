try : import pymysql as cntr
except ImportError : import mysql.connector as cntr
import datetime as __dt , matplotlib.pyplot as plt
from random import shuffle
from tempfile import mktemp
from os import system , startfile

__db = cntr.connect(host = 'localhost' , user = 'sqluser' , passwd = '12345' , database = 'cscproject' , autocommit=True)
__cur = __db.cursor()

#JPP
def add_student() :
    sname = input("Enter the student name : ")
    year = int(input("Enter year of student : "))
    school = input("Enter the School name : ")
    class_sec = input("Enter the Class with Section Example 12A : ")
    email = input("Enter the student email : ")
    mobile = input("Enter the student mobile number : ")
    loginid = input("Enter the student loginid : ")
    loginpwd = input("Enter a Password : ")
    loginpwd2 = input("Enter Password to confirm : ")
    if loginpwd == loginpwd2 :
        __cur.execute("insert into students values('{}' , '{}', '{}' , '{}', '{}' , '{}', '{}' , '{}')".format(sname, year, school, class_sec, email, mobile, loginid, loginpwd))
        print("Student Record Created Successfully!!!")
    elif passwd != passwd2 : print("You've entered different passwords")
#JPP
def add_event() :
    ecode = input("Enter the event code : ")
    ename = input("Enter the event name : ")
    evenue = input("Enter the event venue : ")
    edate  = input("Enter the event date (dd/mm/yyyy) : ")
    etime  = input("Enter the event time (hh:mm AM/PM) : ")
    eduration = int(input("Enter the duration of event (hours) : "))
    cname = input("Enter the co-ordinator name : ")
    __cur.execute("insert into events values('{}' , '{}', '{}' , '{}', '{}' , '{}', '{}')".format(ecode, ename, evenue, edate, etime, eduration, cname))
    print("Created Successfully!!!")
#JPP
def view_event() :
    #data = __cur.fetchall()
    __cur.execute("select ecode, ename, evenue, edate, etime, eduration, cname from events oder by ecode")
    data = __cur.fetchall()
    #print(__cur.rowcount)
    if __cur.rowcount != 0 :
        print("List of Events ===>")
        print("Code Name       Venue            Date        Time       Duration Co-ordinator")
        for row in data :
            print(row[0].center(4," "),'   ',row[1].center(10," "),'   ',row[2].center(10," "),'   ',row[3],'   ',row[4],'   ',row[5],' Hours     ',row[6])
#JPP
def view_student() :
    #data = __cur.fetchall()
    __cur.execute("select sname, year, school, class_sec, email, mobile from students order by sname")
    data = __cur.fetchall()
    #print(__cur.rowcount)
    if __cur.rowcount != 0 :
        print("List of Students ===>")
        print("Name      Year     School         Class/Sec    email            Mobile")
        for row in data :
            print(row[0].center(10," "),'   ',row[1],'    ',row[2].center(10," "),'   ',row[3].center(10," "),'   ',row[4].center(10," "),'   ',row[5])
#JPP
def register_event() :
    ipmobile = input("Enter your mobile number : ")
    sql = f"select * from students where mobile = '{ipmobile}'"
    __cur.execute(sql)
    sql_result = __cur.fetchall()
    print(__cur.rowcount)
    if __cur.rowcount == 0 :
        print("Mobile number not found")
        return bool(__cur.rowcount)

    ipecode = input("Enter the event code : ")
    sql = f"select * from events where ecode = '{ipecode}'"
    __cur.execute(sql)
    sql_result = __cur.fetchall()
    print(__cur.rowcount)
    if __cur.rowcount == 0 :
        print("Event code not found")        
        return bool(__cur.rowcount)

    sql = f"select * from attend where umobile = '{ipmobile}' and ecode = '{ipecode}'"
    __cur.execute(sql)
    sql_result = __cur.fetchall()
    print(__cur.rowcount)
    if __cur.rowcount > 0 :
        print("Already resigered")
        return bool(__cur.rowcount)

    attend = "N"
    __cur.execute("insert into attend values('{}' , '{}', '{}' )".format(ipmobile, ipecode, attend))
    print("Registered Successfully!!!")
    
#JPP
def list_registered() :
    umobile = input("Enter your mobile number : ")
    data = __cur.fetchall()
    __cur.execute("select a.ecode, b.ename, b.evenue, b.edate, b.etime, b.eduration, b.cname from attend a, events b where a.ecode=b.ecode and umobile='{}' order by a.ecode".format(umobile))
    data = __cur.fetchall()
    #print(__cur.rowcount)
    if __cur.rowcount != 0 :
        print("List of Registered Events ===>")
        print("Events Code  Event Name  Venue   Date   Time  Duration-Hrs   Co-ordinator ")
        for row in data :
            #print(row[0], ' ',row[1], '  ', row[2], '  ', row[3], '  ', row[4], '  ', row[5], '  ', row[6])
            print(row[0],row[1], row[2], row[3], row[4], row[5], row[6], sep='      ')
#JPP
def view_battend() :
    ecode = input("Enter the event code : ")
    filename = mktemp('.txt')
    #data = __cur.fetchall()
    __cur.execute("select ecode, ename, evenue, edate, etime, eduration, cname from events where ecode='{}'".format(ecode))
    data = __cur.fetchall()
    #print(__cur.rowcount)
    if __cur.rowcount != 0 :
       for row in data :
           q = '''Event *Initial* Attendance\nCode         : {}\nName         : {}\nVenue        : {}\nDate         : {}\nTime         : {}\nDuration     : {} Hours\nCo-Ordinator : {}\n\n\n'''.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
           open(filename , 'w').write(q)
           #startfile(filename , 'print')

    data1 = __cur.fetchall()
    __cur.execute("select umobile from attend where ecode='{}' order by umobile".format(ecode))
    row1 = __cur.rowcount
    data1 = __cur.fetchall()
    q1 = '''Name            Yr School & Class/Sec      email         Mobile         Sign \n'''
    open(filename , 'a').write(q1)
    #startfile(filename , 'print')
    if row1 > 0 :
        for row in data1 :
            data2 = __cur.fetchall()
            __cur.execute("select sname, year, school, class_sec, email, mobile from students where mobile='{}' order by mobile".format(row[0]))
            row2 = __cur.rowcount
            data2 = __cur.fetchall()
            for row2 in data2 :
                q1 = '''{} {}  {}-{}         {}    {}   \n'''.format(row2[0].center(15," "), row2[1], row2[2], row2[3], row2[4].center(10," "), row2[5])
                open(filename , 'a').write(q1)
                #startfile(filename , 'print')
    startfile(filename , 'print')
#JPP
def view_fattend() :
    ecode = input("Enter the event code : ")
    filename = mktemp('.txt')
    #data = __cur.fetchall()
    __cur.execute("select ecode, ename, evenue, edate, etime, eduration, cname from events where ecode='{}'".format(ecode))
    data = __cur.fetchall()
    #print(__cur.rowcount)
    if __cur.rowcount != 0 :
       for row in data :
           q = '''Event *FINAL* Attendance\nCode         : {}\nName         : {}\nVenue        : {}\nDate         : {}\nTime         : {}\nDuration     : {} Hours\nCo-Ordinator : {}\n\n\n'''.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
           open(filename , 'w').write(q)
           #startfile(filename , 'print')

    data1 = __cur.fetchall()
    __cur.execute("select umobile from attend where ecode='{}' and attend='Y' order by umobile".format(ecode))
    row1 = __cur.rowcount
    data1 = __cur.fetchall()
    q1 = '''Name            Yr school & class_sec      Email        Mobile          Att \n'''
    open(filename , 'a').write(q1)
    #startfile(filename , 'print')
    if row1 > 0 :
        for row in data1 :
            data2 = __cur.fetchall()
            __cur.execute("select sname, year, school, class_sec, email, mobile from students where mobile='{}' order by mobile".format(row[0]))
            row2 = __cur.rowcount
            data2 = __cur.fetchall()
            for row2 in data2 :
                q1 = '''{} {}  {}-{}     {}       {}   Y\n'''.format(row2[0].center(15," "), row2[1], row2[2], row2[3], row2[4].center(10," "), row2[5])
                open(filename , 'a').write(q1)
                #startfile(filename , 'print')
    startfile(filename , 'print')

#JPP
def enter_attend() :
    ecode = input("Enter the event code : ")
    #data = __cur.fetchall()
    __cur.execute("select ecode, ename, evenue, edate, etime, eduration, cname from events where ecode='{}'".format(ecode))
    data = __cur.fetchall()
    if __cur.rowcount != 0 :
       mobile =  "1234567890"
       while mobile != "" :
            mobile = input("Enter Student's Mobile Number (Empty to exit) : ")
            __cur.execute("update attend set attend = 'Y' where umobile = '{}'".format(mobile))
    else : print("Invalid Event Code ... ")

    print("Attendance entered successfully .... ")
#JPP           
def login():
    user = input("Enter the student username : ")
    pwd = input("Enter the student password : ")
#   __cur.execute("select * from users where username = '{}' and password = '{}'".format(user , pwd))
#    __cur.execute("select * from users where username = %s and password = %s", (user , pwd))
    sql = f"select * from students where loginid = '{user}' and loginpwd = '{pwd}'"
    __cur.execute(sql)
    sql_result = __cur.fetchall()
    print(__cur.rowcount)
    return bool(__cur.rowcount)
