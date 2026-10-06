from flask import Flask, request, render_template
import main as execute

import database.editprojects as edit_project
import database.editcustomer as edit_customer
import database.editmanager as edit_manager

app = Flask(__name__)

# WELCOME PAGE
@app.route('/')

def index():

    return render_template("index.html")

# LIST ALL PROJECTS
@app.route('/showall', methods = ['POST'])

def showall():

    local_all_data = edit_project.showall()

    return render_template("showall.html", web_all_data = local_all_data)

# CREATE NEW PROJECT
@app.route('/new_project', methods = ['POST'])

def new_project():

    return render_template("new_project.html", msg = "Enter project details:")

@app.route('/create_project', methods = ['POST'])

def create_project():

    if request.method == 'POST':
        local_data = request.form.to_dict(flat = False)

    status = execute.create_project(local_data)

    if status == 1:
        return render_template("new_project.html", msg = "Customer not found")
    elif status == 2:
        return render_template("new_project.html", msg = "Manager not found")
    else:
        return render_template("index.html")

app.run(debug = True)