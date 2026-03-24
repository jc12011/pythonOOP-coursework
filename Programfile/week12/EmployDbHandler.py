from EmployeeClass import WorkerClass, SupervisorClass
import pickle
class EmployDbHandler:
    def __init__(self):
        try:
            datafile=open('EmployDb.dat','rb')
            self.data=pickle.load(datafile)
            datafile.close()
        except FileNotFoundError:
            self.data={}
            
    def add_modify_employee(self,employee):
        self.data[employee.id]=employee

    def del_employee(self, employee_id):
        del self.data[employee_id]

    def look_up_employee(self, employee_id):
        if employee_id in self.data:
            print("Look up success.")
            return self.data[employee_id]
        if employee_id not in self.data:
            print("Look up fail! No such employee!")
            return False

    def list_all_employee(self):
        #for key in self.data:
        #    print(self.data[key])
        return(self.data.keys())

    def check_if_exist(self, employee_id):
        if employee_id not in self.data:
            return False
        elif employee_id in self.data:
            return True

    def save(self):
        output_file=open('EmployDb.dat', 'wb')
        pickle.dump(self.data, output_file)
        output_file.close()