class LookUpEmployee:
    def __init__(self,db_handler):
        self.db_handler = db_handler
    def execute(self):
        employee_id = input('Please enter the employee_id: ')
        if self.db_handler.check_if_exist(employee_id) is True:
            print(self.db_handler.look_up_employee(employee_id))
        else:
            print("The employee does not exist.")
