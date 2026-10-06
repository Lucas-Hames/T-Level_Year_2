import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "projects")

def _check_id_integrity(customer_id, manager_id):
    
    with sqlite3.connect(DB_PATH) as conn:

        customer = conn.execute("""
            SELECT forename
            FROM tbl_customer
            WHERE customer_id = ?
        """, (customer_id, )).fetchone()

        manager = conn.execute("""
            SELECT forename
            FROM tbl_manager
            WHERE manager_id = ?
        """, (manager_id, )).fetchone()

        if customer == None and manager == None:
            return 3
        elif manager == None:
            return 2
        elif customer == None:
            return 1
        else:
            return 0

def find_project(project_id):

    with sqlite3.connect(DB_PATH) as conn:

        project = conn.execute("""
            SELECT *
            FROM tbl_project
            WHERE project_id = ?
        """, (project_id, )).fetchall()

        return project

def add_project(project_type_id, customer_id, manager_id, planned_start_date, actual_start_date, trades_people_amount):

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            INSERT INTO tbl_project( 
                project_type_id, 
                customer_id, 
                manager_id, 
                planned_start_date, 
                actual_start_date, 
                trades_people_amount
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, ( 
            project_type_id, 
            customer_id, 
            manager_id, 
            planned_start_date, 
            actual_start_date, 
            trades_people_amount
        ))
        conn.commit()
        print("SUCCESSFULLY SAVED TO DATABASE")

def edit_project(project_id, project_type_id, customer_id, manager_id, planned_start_date, actual_start_date, trades_people_amount):

    integrity = _check_id_integrity(customer_id, manager_id)
    if integrity != 0:
        return integrity

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            UPDATE tbl_project
            SET
                project_type_id = ?,
                customer_id = ?,
                manager_id = ?, 
                planned_start_date = ?, 
                actual_start_date = ?, 
                trades_people_amount = ?
            WHERE project_id = ?
        """, (
            project_type_id, 
            customer_id, 
            manager_id, 
            planned_start_date, 
            actual_start_date, 
            trades_people_amount,
            project_id
        ))
        conn.commit()

        return integrity

def delete_project(project_id):

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            DELETE FROM tbl_project
            WHERE project_id = ?
        """, (project_id, ))
        conn.commit()

def showall():

    with sqlite3.connect(DB_PATH) as conn:

        all_data = conn.execute("""
            SELECT *
            FROM tbl_project, tbl_project_type, tbl_customer, tbl_manager
            WHERE tbl_project_type.project_type_id = tbl_project.project_type_id
            AND tbl_customer.customer_id = tbl_project.customer_id
            AND tbl_manager.manager_id = tbl_project.manager_id
        """).fetchall()

        return all_data