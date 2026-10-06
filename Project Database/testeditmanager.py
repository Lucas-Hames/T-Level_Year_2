import database.editmanager as edit_manager

def test_edit_manager():

    def _find():
        manager_id = input("ID: ")
        forename = input("Forename: ")
        surname = input("Surname: ")
        manager = edit_manager.find_manager(manager_id, forename, surname)
        print(manager)

    def _add():
        forename = input("Forename: ")
        surname = input("Surname: ")
        edit_manager.add_manager(forename, surname)

    def _edit():
        manager_id = input("ID: ")
        forename = input("Forename: ")
        surname = input("Surname: ")
        edit_manager.edit_manager(manager_id, forename, surname)

    def _delete():
        manager_id = input("ID: ")
        edit_manager.delete_manager(manager_id)

    def _showall():
        all_data = edit_manager.showall()
        for i in all_data:
            print(i[0], i[1], i[2])

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
    test_edit_manager()