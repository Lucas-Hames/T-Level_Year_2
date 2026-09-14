from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')

def index():

    now = datetime.now()
    formatted_now = now.strftime("%d/%m/%Y")

    return render_template('index.html', webvar = formatted_now)

@app.route('/afterlogin', methods = ['POST'])

def login():

    if request.method == "POST":
        local_uname = request.form.get("uname")
        local_pwd = request.form.get("pwd")

    print("reached login page")
    return render_template('welcome.html', web_uname = local_uname, web_pwd = local_pwd)

if __name__ == '__main__':
    app.run(debug = True)