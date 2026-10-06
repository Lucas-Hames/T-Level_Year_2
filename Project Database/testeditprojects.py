import database.editprojects as edit_project

def test_edit_project():

    def _alert_integrity(integrity):
        match integrity:
            case 1:
                print("Customer ID not recognised")
            case 2:
                print("Manager ID not recognised")
            case 3:
                print("Customer and Manager ID not recognised")

    def _find():
        project_id = input("ID: ")
        project = edit_project.find_project(project_id)
        print(project)

    def _add():
        project_type_id = input("Type ID: ")
        customer_id = input("Customer ID: ")
        manager_id = input("Manager ID: ")
        planned_start_date = input("Planned Start Date: ")
        actual_start_date = input("Actual Start Date: ")
        trades_people_amount = input("Amount of Trades People: ")
        integrity = edit_project.add_project(project_type_id, customer_id, manager_id, planned_start_date, actual_start_date, trades_people_amount)
        if integrity != 0:
            _alert_integrity(integrity)

    def _edit():
        project_id = input("ID: ")
        project_type_id = input("Type ID: ")
        customer_id = input("Customer ID: ")
        manager_id = input("Manager ID: ")
        planned_start_date = input("Planned Start Date: ")
        actual_start_date = input("Actual Start Date: ")
        trades_people_amount = input("Amount of Trades People: ")
        integrity = edit_project.edit_project(project_id, project_type_id, customer_id, manager_id, planned_start_date, actual_start_date, trades_people_amount)
        if integrity != 0:
            _alert_integrity(integrity)

    def _delete():
        project_id = input("ID: ")
        edit_project.delete_project(project_id)

    def _showall():
        all_data = edit_project.showall()
        for i in all_data:
            print(i[0], i[1], i[2], i[3], i[4], i[5], i[6])

    choice = input("A: Find\nB: Add\nC: Edit\nD: Delete\nE: Showall\n").upper()

    match choice:
        case 'A':
            _find()
            return
        case 'B':
            _add()
            return
        case 'C':
            _edit()
            return
        case 'D':
            _delete()
            return
        case 'E':
            _showall()
            return

while __name__ == "__main__":
    test_edit_project()