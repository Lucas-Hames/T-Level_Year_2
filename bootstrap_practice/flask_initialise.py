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
        return render_template('welcome.html', web_uname = local_uname, web_pwd = local_pwd)
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
        
        return render_template('welcome.html', web_uname = local_uname, web_pwd = local_new_pwd)

# --- REGISTRATION PAGE ---

@app.route('/register')

def register():
    return render_template('register.html')

@app.route('/register_user', methods = ['POST'])

def register_user():
    
    local_uname = request.form.get("uname")
    local_pwd = request.form.get("pwd")

    with sqlite3.connect("users") as conn:
        users = conn.execute("""
            SELECT *
            FROM tbl_users
            WHERE username = ?
        """, (local_uname,)).fetchone()

    if users != None:
        return render_template('welcome.html', web_uname = local_uname, web_pwd = local_pwd)
    else:

        with sqlite3.connect("users") as conn:
            conn.execute("""
                INSERT INTO tbl_users(username, password)
                VALUES(?, ?)
            """, (local_uname, local_pwd))
            conn.commit()

        return render_template('welcome_new.html', web_uname = local_uname, web_pwd = local_pwd)

# --- SHOWALL ---

@app.route('/showall')

def showall():

    with sqlite3.connect("users") as conn:
        users = conn.execute("""
            SELECT *
            FROM tbl_users
        """).fetchall()

    return render_template('showall.html', web_all_users = users)

if __name__ == '__main__':
    app.run(debug = True)