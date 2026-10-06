import database.editprojects as edit_project
import database.editcustomer as edit_customer
import database.editmanager as edit_manager

def create_project(all_data):

    customer = all_data["customer"][0]
    customer_data = None
    manager = all_data["manager"][0]
    manager_data = None

    if " " in customer:
        name = []
        name.append(str(customer).split(" "))
        customer_data = edit_customer.find_customer(None, name[0], surname = list_to_string(name[1:], " "))
        if customer_data == None:
            return 1

    if " " in manager:
        name = []
        name.append(str(manager).split(" "))
        manager_data = edit_manager.find_manager(None, name[0], surname = list_to_string(name[1:], " "))
        if manager_data == None:
            return 2

    if customer_data == None:
        customer_data = edit_customer.find_customer(customer, customer, customer)
        if customer_data == None:
            return 1

    if manager_data == None:
        manager_data = edit_manager.find_manager(manager, manager, manager)
        if manager_data == None:
            return 2

    # DISCLAIMER all_data PARAMETERS MUST MATCH ID OF new_project.html
    edit_project.add_project(
        all_data["project_type"][0], 
        str(customer_data[0]), 
        str(manager_data[0]), 
        all_data["planned_date"][0], 
        all_data["actual_date"][0], 
        all_data["no_trades_ppl"][0]
    )

    return 0