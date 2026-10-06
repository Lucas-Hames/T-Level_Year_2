import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "projects")

def find_customer(customer_id, forename, surname):

    with sqlite3.connect(DB_PATH) as conn:
        
        customer = conn.execute("""
            SELECT *
            FROM tbl_customer
            WHERE customer_id = ?
                OR forename = ?
                OR surname = ?
        """, (customer_id, forename, surname)).fetchall()

        return customer

def add_customer(forename, surname, telephone):

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            INSERT INTO tbl_customer(
                forename,
                surname,
                telephone
            )
            VALUES (?, ?, ?)
        """, (forename, surname, telephone))
        conn.commit()

def edit_customer(customer_id, forename, surname, telephone):

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            UPDATE tbl_customer
            SET forename = ?, surname = ?, telephone = ?
            WHERE customer_id = ?
        """, (forename, surname, telephone, customer_id))
        conn.commit()

def delete_customer(customer_id):

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            DELETE FROM tbl_customer
            WHERE customer_id = ?
        """, (customer_id, ))
        conn.commit()

def showall():

    with sqlite3.connect(DB_PATH) as conn:

        all_data = conn.execute("""
            SELECT *
            FROM tbl_customer
        """).fetchall()

        return all_data