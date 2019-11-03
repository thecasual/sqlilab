from flask import Flask, render_template, request
import re
from inject import *
labregex = "^lab\d+$"
app = Flask(__name__)

#TODO
# 1) UI
# 2) Button - Rebuild all labs
# 3) Button - rebuild a single lab
# 4) Create submission - same query for all labs?

@app.route('/')
def hello():
    return render_template('lablanding.html')

@app.route('/<string:page_name>/', methods=['GET', 'POST'])
def render_static(page_name):

    if re.match(labregex, page_name):
        labnum = re.sub("\D", "", page_name)

    #Answer Attempt
    if request.method == 'POST' and request.form.get('answer'):
        answer = request.form.get('answer')
        return "Answer submitted {}".format(answer)

    #SQL Injection attempts go here
    elif request.method == 'POST' and request.form.get('value') and request.form.get('lab'):
        value = request.form.get('value')
        labinstance = request.form.get('lab')

        result = processrequest(labnum, value)
        if result != "No results":
            msg = ""
            for entry in result:
                msg = msg + entry[2] + '\n'
            return render_template('lab.html', labname=page_name, labnum=labnum, returndata=msg)
        #If there is no data in the sql query
        else:
            return render_template('lab.html', labname=page_name, labnum=labnum, returndata="No results")

    #Landing
    elif re.match(labregex, page_name):
        return render_template('lab.html', labname=page_name, labnum=labnum, returndata="return data here")
        #else:
        #    return "You shouldn't be here"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')