import pickle
class ListAllEmployee:
    def __init__(self,db_handler):
        self.db_handler=db_handler
        
    def execute(self):
        #self.db_handler=open('EmployDb.dat','rb')
        #Employee_data=pickle.load(self.db_handler)
        #self.db_handler.close()
        employee_list=self.db_handler.list_all_employee()
        for key in employee_list:
            print(self.db_handler.look_up_employee(key))
        #for key in Employee_data:
        #    print(Employee_data[key])