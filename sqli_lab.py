from flask import Flask, render_template, request, send_from_directory, json, make_response
import re
from inject import *
from util import *
labregex = "^lab\d+$"
app = Flask(__name__)

with open('sqlilab.json') as json_data_file:
    data = json.load(json_data_file)
    
@app.route('/')
def hello():
    if "sqlilab" not in request.cookies:
        return render_template('signup.html') 
    return render_template('lablanding.html', custommessage="")

@app.route('/rebuildlab')
def rebuild():
    print("Rebuilding Lab")
    rebuildeverything()
    return render_template('lablanding.html', custommessage="Lab has been rebuilt!")

@app.route('/score.json')
def returnscorejson():
    return render_template('score.json')

@app.route('/wallofshame.json')
def returnwallofshamejson():
    return render_template('wallofshame.json')

@app.route('/wallofshame')
def returnwallofshame():
    return render_template('wallofshame.html')

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
        resp = make_response(render_template('lablanding.html', custommessage=""))
        resp.set_cookie('sqlilab', key)
        return resp
    elif "sqlilab" in request.cookies:
        key = request.cookies['sqlilab']
        username = getuserfromkey(key)
        return render_template('lablanding.html', custommessage="You already have an account called {}".format(username))
    else:
        print("Who are you...")
        return render_template('signup.html')

@app.route('/<string:page_name>/', methods=['GET', 'POST'])
def render_static(page_name):

    if "sqlilab" not in request.cookies:
        return render_template('signup.html') 

    labsbuilt = len(data['labs'][0])

    if re.match(labregex, page_name):
        labnum = re.sub("\D", "", page_name)
        sqlquery = data['labs'][0][labnum]['Query']
        refilter = data['labs'][0][labnum]['Filter']

    #Answer Attempt
    if request.method == 'POST' and request.form.get('answer'):
        answer = request.form.get('answer')
        if checkanswer(labnum, answer):
            if "sqlilab" not in request.cookies:
               return render_template('signup.html') 
            else:
                #Correct answer provided
                updatescore(labnum, request.cookies['sqlilab'])
                
                user = getuserfromkey(request.cookies['sqlilab'])
                ChallengeURL = data['config']['ChallengeURL']
                try:
                    postwebhook("Flag Captured!! Challenge {0} Completed By {1}\r\rJOIN HERE: {2}\r\rSCOREBOARD: {3}".format(labnum, user, ChallengeURL, "{}score".format(ChallengeURL)))
                except:
                    pass
                return render_template('lab.html',  labsbuilt=labsbuilt, labname=page_name, sqlquery=sqlquery, refilter=refilter, labnum=labnum, returndata="Nice Work!!! Bobby would be so proud of you!")
        else:
            return render_template('lab.html',  labsbuilt=labsbuilt, labname=page_name, sqlquery=sqlquery, refilter=refilter, labnum=labnum, returndata="Incorrect Answer!")

    #SQL Injection attempts go here
    elif request.method == 'POST' and request.form.get('value') and request.form.get('lab'):
        value = request.form.get('value')
        labinstance = request.form.get('lab')
        user = getuserfromkey(request.cookies['sqlilab'])
        result = processrequest(labnum, value, user)
        if result != "No results":
            #msg = ""
            #for entry in result:
            #    msg = msg + entry[2] + '\n'
            return render_template('lab.html',  labsbuilt=labsbuilt, labname=page_name, sqlquery=sqlquery, refilter=refilter, labnum=labnum, returndata=result)
        #If there is no data in the sql query
        else:
            return render_template('lab.html',  labsbuilt=labsbuilt, labname=page_name, sqlquery=sqlquery, refilter=refilter, labnum=labnum, returndata="No results")

    #Landing
    elif re.match(labregex, page_name):
        return render_template('lab.html',  labsbuilt=labsbuilt, labname=page_name, sqlquery=sqlquery, refilter=refilter, labnum=labnum, returndata="")
        #else:
        #    return "You shouldn't be here"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')