class DelEmployee:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def execute(self):
        employee_id = str(input('Enter the emplyee id: '))
        if self.db_handler.check_if_exist(employee_id) is True:
            self.db_handler.del_employee(employee_id)
            print('Entry deleted.')
        else:
            print('That ID is not found.')

