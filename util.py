import json
import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def usersignup(username):
    with open('users.json') as json_file:
        data = json.load(json_file)
        exists = False
        for n in data:
            if username == n['Name']:
                exists = True
                return n['Key']
    if exists == False:
        print("Creating user {}".format(username))
        key = randomString()
        data.append({
            'Name' : username,
             'Key' : key
            })
        with open('users.json', 'w') as out:
            json.dump(data, out)
        return key       

def getuserfromkey(key):
    found = False
    with open('users.json') as json_file:
        data = json.load(json_file)
    for n in data:
        if key == n['Key']:
            found = True
            return n['Name']
    if found == False:
        return "Invalid key"
         

def updatescore(labnum, key):
    with open('templates/score.json') as json_file:
        data = json.load(json_file)
    username = getuserfromkey(key)
    flag = "Flag {}".format(labnum)
    found = False

    for n in data:
        if username == n['Name']:
            if flag in n:
                print("Flag already acquired")
                found = True
                return "Flag already acquired"
    if found == False:
        c = 0
        for j in data:
            if username == j['Name']:
                data[c][flag] = "True"
                with open('score.json', 'w') as out:
                    json.dump(data, out)
                break
            c+=1


updatescore("4", "123124124213")
