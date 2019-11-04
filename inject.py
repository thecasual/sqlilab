import json
import mysql.connector
import re

# From config load filter + sql query and then return results to user

with open('sqlilab.json') as json_data_file:
    data = json.load(json_data_file)

dbhost = data['config']['dbhost']
uname = data['config']['username']
pwd = data['config']['password']
dbname = data['config']['database']

#Access Lab 2 - data['labs'][0]['2']

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
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    
    if len(myresult) == 0:
        return "No results"
    else:
        #print("Returning {}".format(myresult))
        return myresult

def processrequest(labnum, value):
    if labnum in data['labs'][0] and len(value) > 0:
        f = data['labs'][0][labnum]['Filter']
        cleanvalue = re.sub(f, '', value)
        query = data['labs'][0][labnum]['Query']
        query = query.replace('USERINPUTHERE', cleanvalue)
        out = sqlquery(labnum, query)
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

# 1) 1' UNION SELECT Name, Password FROM secret -- -