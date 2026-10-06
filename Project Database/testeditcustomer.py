import database.editcustomer as edit_customer

def test_edit_customer():

    def _find():
        customer_id = input("ID: ")
        forename = input("Forename: ")
        surname = input("Surname: ")
        customer = edit_customer.find_customer(customer_id, forename, surname)
        print(customer)

    def _add():
        forename = input("Forename: ")
        surname = input("Surname: ")
        telephone = input("Telephone: ")
        edit_customer.add_customer(forename, surname, telephone)

    def _edit():
        customer_id = input("ID: ")
        forename = input("Forename: ")
        surname = input("Surname: ")
        telephone = input("Telephone: ")
        edit_customer.edit_customer(customer_id, forename, surname, telephone)

    def _delete():
        customer_id = input("ID: ")
        edit_customer.delete_customer(customer_id)

    def _showall():
        all_data = edit_customer.showall()
        for i in all_data:
            print(i[0], i[1], i[2], i[3])

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
    test_edit_customer()