import sqlite3

def test():

    with sqlite3.connect("projects") as conn:

        conn.execute("""
            INSERT INTO tbl_project_type(project_type)
            VALUES ("Kitchen")
        """)
        conn.commit()

        conn.execute("""
            INSERT INTO tbl_project_type(project_type) 
            VALUES ("Bathroom")
        """)
        conn.commit()

        data = conn.execute("""
            SELECT *
            FROM tbl_project_type
        """)

        for i in data:
            print(i[0], i[1])

def reset():

    with sqlite3.connect("projects") as conn:

        conn.execute("""
            DELETE FROM tbl_project_type
        """)
        conn.commit()

reset()