import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "projects")

def find_manager(manager_id, forename, surname):

    with sqlite3.connect(DB_PATH) as conn:
        
        manager = conn.execute("""
            SELECT *
            FROM tbl_manager
            WHERE manager_id = ?
                OR forename = ?
                OR surname = ?
        """, (manager_id, forename, surname)).fetchall()

        return manager

def add_manager(forename, surname):

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            INSERT INTO tbl_manager(
                forename,
                surname
            )
            VALUES (?, ?)
        """, (forename, surname))
        conn.commit()

def edit_manager(manager_id, forename, surname):

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            UPDATE tbl_manager
            SET forename = ?, surname = ?
            WHERE manager_id = ?
        """, (forename, surname, manager_id))
        conn.commit()

def delete_manager(manager_id):

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            DELETE FROM tbl_manager
            WHERE manager_id = ?
        """, (manager_id, ))
        conn.commit()

def showall():

    with sqlite3.connect(DB_PATH) as conn:

        all_data = conn.execute("""
            SELECT *
            FROM tbl_manager
        """).fetchall()

        return all_data