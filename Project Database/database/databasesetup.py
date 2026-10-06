import sqlite3

def setup():

    with sqlite3.connect("projects") as conn:

        conn.execute("""
            CREATE TABLE tbl_project_type(
                project_type_id integer PRIMARY KEY AUTOINCREMENT,
                project_type text NOT NULL
            )
        """)
        conn.commit()

        conn.execute("""
            CREATE TABLE tbl_customer(
                customer_id integer PRIMARY KEY AUTOINCREMENT,
                forename varchar(255),
                surname varchar(255),
                telephone text
            )
        """)
        conn.commit()

        conn.execute("""
            CREATE TABLE tbl_manager(
                manager_id integer PRIMARY KEY AUTOINCREMENT,
                forename varchar(255),
                surname varchar(255)
            )
        """)
        conn.commit()

        conn.execute("""
            CREATE TABLE tbl_project(
                project_id integer PRIMARY KEY AUTOINCREMENT,
                project_type_id integer,
                customer_id integer,
                manager_id integer,
                planned_start_date text,
                actual_start_date text,
                trades_people_amount integer,

                FOREIGN KEY (project_type_id)
                    REFERENCES tbl_project_type(project_type_id),
                FOREIGN KEY (customer_id)
                    REFERENCES tbl_customer(customer_id),
                FOREIGN KEY (manager_id)
                    REFERENCES tbl_manager(manager_id)
            )
        """)
        conn.commit()

        print("Successfully created database")

def input_project_data():

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

setup()
input_project_data()