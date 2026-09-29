import sqlite3
import json

languages = ["Python", "HTML"]

conn = sqlite3.connect("users")

def setup():
    conn.execute("""
        CREATE TABLE tbl_users(
            username varchar(255),
            email varchar(255),
            password varchar(255),
            age int,
            website varchar(255),
            date_of_birth varchar(255),
            gender varchar(255),
            languages varchar(255)
        )
    """)

def add_users():
    conn.execute("""
        INSERT INTO tbl_users(username, email, password, age, website, date_of_birth, gender, languages)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?)
    """,("Lucas", "s2334911@students.southwark.ac.uk", "password", 19, "http://www.testsite.com", "2007-09-04", "Male", json.dumps(languages)))
    conn.commit()

def showall():
    data = conn.execute("""
        SELECT *
        FROM tbl_users
    """)

    for column in data:
        print(
            f"Name: {column[0]}\n"
            f"Email: {column[1]}\n"
            f"Password: {column[2]}\n"
            f"Age: {column[3]}\n"
            f"Website: {column[4]}\n"
            f"Date of Birth: {column[5]}\n"
            f"Gender: {column[6]}\n"
            f"Languages: {column[7]}"
        )

setup()
add_users()
showall()

conn.close()