from flask import Flask, request, render_template, session
from datetime import datetime
import sqlite3
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# --- MAIN PAGE ---

@app.route('/')

def index():

    now = datetime.now()
    formatted_now = now.strftime("%d/%m/%Y")

    return render_template('index.html', webvar = formatted_now)

@app.route('/afterlogin', methods = ['POST'])

def login():

    local_uname = request.form.get("uname")
    local_pwd = request.form.get("pwd")

    with sqlite3.connect("users") as conn:
        users = conn.execute("""
            SELECT *
            FROM tbl_users
            WHERE username = ? AND password = ?
        """, (local_uname, local_pwd)).fetchone()

    if users != None:
        session["username"] = local_uname
        session["password"] = local_pwd
        return render_template('welcome.html', web_uname = local_uname)
    else:
        return render_template('not_found.html')

@app.route('/delete', methods = ['POST'])

def delete_user():

    local_uname = session.get("username")

    with sqlite3.connect("users") as conn:
        conn.execute("""
            DELETE FROM tbl_users
            WHERE username = ?
        """, (local_uname,))
        conn.commit()

    return render_template('delete.html', web_uname = local_uname)

# --- CHANGE PASSWORD ---

@app.route('/change_password', methods = ['POST'])

def change_password():
    return render_template('change_password.html', message = "Change Password")

@app.route('/confirm_password', methods = ['POST'])

def confirm_password():

    local_uname = session.get("username")
    local_pwd = session.get("password")
    local_old_pwd = request.form.get("old_pwd")
    local_new_pwd = request.form.get("new_pwd")
    local_confirm_pwd = request.form.get("confirm_pwd")

    if local_pwd != local_old_pwd or local_new_pwd != local_confirm_pwd:
        return render_template('change_password.html', message = "Error: Please try again")
    else:

        with sqlite3.connect('users') as conn:
            conn.execute("""
                UPDATE tbl_users
                SET password = ?
                WHERE username = ?
            """, (local_new_pwd, local_uname))
            conn.commit()
        
        return render_template('welcome.html', web_uname = local_uname)
        welcome()

# --- REGISTRATION PAGE ---

@app.route('/register')

def register():
    return render_template('register.html', header = "Register")

@app.route('/register_user', methods = ['POST'])

def register_user():
    
    if request.method == 'POST':
        data = request.form.to_dict(flat = False)
        print(data)

    with sqlite3.connect("users") as conn:
        users = conn.execute("""
            SELECT *
            FROM tbl_users
            WHERE username = ? OR email = ?
        """, (data['uname'][0], data['email'][0])).fetchone()

    if users != None:
        return render_template('register.html', header = "Name or Email already in use.")
    else:

        languages = ', '.join(data['lang'])

        with sqlite3.connect("users") as conn:
            conn.execute("""
                INSERT INTO tbl_users(username, email, password, age, website, date_of_birth, gender, languages)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?)
            """, (data['uname'][0], data['email'][0], data['pwd'][0], data['age'][0], data['site'][0], data['dob'][0], data['gender'][0], languages))
            conn.commit()

        return render_template('welcome_new.html', web_uname = data['uname'][0])

# --- SHOWALL ---

@app.route('/showall', methods = ['POST'])

def showall():

    local_uname = request.form.get('uname')

    with sqlite3.connect("users") as conn:
        users = conn.execute("""
            SELECT *
            FROM tbl_users
            WHERE username = ?
        """, (local_uname, )).fetchall()

    print(f"USERS: {users}")

    return render_template('showall.html', web_all_users = users)

@app.route('/welcome', methods = ['POST'])

def return_to_welcome():

    local_uname = request.form.get('uname')

    return render_template('welcome.html', web_uname = local_uname)

if __name__ == '__main__':
    app.run(debug = True)