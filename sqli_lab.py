from flask import Flask, render_template, request, send_from_directory, json, make_response
import re
from inject import *
from util import *
labregex = "^lab\d+$"
app = Flask(__name__)

#TODO
# 1) UI
# 2) Button - Rebuild all labs
# 3) Button - rebuild a single lab
# 4) If correct - update score.json
# 5) Webhook when correct

@app.route('/')
def hello():
    return render_template('lablanding.html')

@app.route('/rebuildlab')
def rebuild():
    print("Rebuilding Lab")
    rebuildeverything()
    return render_template('lablanding.html')

@app.route('/score.json')
def returnjson():
    return render_template('score.json')

@app.route('/score')
def returnscore():
    return render_template('score.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST' and request.form.get('username'):
        username = request.form.get('username')
        print(username)
        key = usersignup(username)
        resp = make_response(render_template('lablanding.html'))
        resp.set_cookie('sqlilab', key)
        return resp
    elif "sqlilab" in request.cookies:
        key = request.cookies['sqlilab']
        username = getuserfromkey(key)
        return "You are already signed up... \r Username {} : Key {}".format(username,key)
    else:
        print("Who are you...")
        return render_template('signup.html')

@app.route('/<string:page_name>/', methods=['GET', 'POST'])
def render_static(page_name):

    if re.match(labregex, page_name):
        labnum = re.sub("\D", "", page_name)

    #Answer Attempt
    if request.method == 'POST' and request.form.get('answer'):
        answer = request.form.get('answer')
        if checkanswer(labnum, answer):
            if "sqlilab" not in request.cookies:
               return render_template('signup.html') 
            else:
                updatescore(labnum, request.cookies['sqlilab'])
                return render_template('lab.html', labname=page_name, labnum=labnum, returndata="Nice Work!!! Bobby would be so proud of you!")
                #return "Correct answer provided"
                #Correct answer provided
                #TODO webhook/update scoreboard
        else:
            return render_template('lab.html', labname=page_name, labnum=labnum, returndata="Incorrect Answer!")

    #SQL Injection attempts go here
    elif request.method == 'POST' and request.form.get('value') and request.form.get('lab'):
        value = request.form.get('value')
        labinstance = request.form.get('lab')

        result = processrequest(labnum, value)
        if result != "No results":
            #msg = ""
            #for entry in result:
            #    msg = msg + entry[2] + '\n'
            return render_template('lab.html', labname=page_name, labnum=labnum, returndata=result)
        #If there is no data in the sql query
        else:
            return render_template('lab.html', labname=page_name, labnum=labnum, returndata="No results")

    #Landing
    elif re.match(labregex, page_name):
        return render_template('lab.html', labname=page_name, labnum=labnum, returndata="")
        #else:
        #    return "You shouldn't be here"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')