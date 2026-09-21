import sqlite3

conn = sqlite3.connect("users")

def setup():
    conn.execute("""
        CREATE TABLE tbl_users(
            username varchar(255),
            password varchar(255)
        )
    """)

def add_users():
    conn.execute("""
        INSERT INTO tbl_users(username, password)
        VALUES("LucasHames", "mika567")
    """)
    conn.commit()

def showall():
    data = conn.execute("""
        SELECT *
        FROM tbl_users
    """)

    for column in data:
        print(f"Name: {column[0]} Password: {column[1]}")

#setup()
#add_users()
showall()

conn.close()