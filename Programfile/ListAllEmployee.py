import pickle
class ListAllEmployee:
    def __init__(self,db_handler):
        self.db_handler=db_handler
        
    def execute(self):
        employee_list=self.db_handler.list_all_employee()
        if(employee_list!=[]):
            for key in employee_list:
                print(self.db_handler.look_up_employee(key))
        else:
            print("Empty List.")