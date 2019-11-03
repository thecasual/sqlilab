from flask import Flask, render_template, request
import re
from inject import *
labregex = "^lab\d+$"
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('lablanding.html')

@app.route('/<string:page_name>/', methods=['GET', 'POST'])
def render_static(page_name):
    if re.match(labregex, page_name):
        labnum = re.sub("\D", "", page_name)

    if request.method == 'POST':
        value = request.form.get('value')
        labinstance = request.form.get('lab')

        if (value, labinstance):
            result = processrequest(labnum, value)
            msg = ""
            for entry in result:
                #print(entry[2])
                msg = msg + entry[2] + '\n'
            return msg
            return "{}".format(result)
        else:
            return "Something went wrong here"

    elif re.match(labregex, page_name):
        return render_template('lab.html', labname=page_name, labnum=labnum)
    else:
        return "You shouldn't be here"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')