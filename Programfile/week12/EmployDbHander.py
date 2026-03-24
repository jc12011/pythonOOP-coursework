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
             print("Loop up success.")
             print(self.data[employee_id])
        if employee_id not in self.data:
            print("Loop up fail! No such employee!")
    def list_all_emplyee(self):
        for key in self.data:
                    print(self.data[key])
    def check_if_exist(self, employee_id):
        if employee_id not in self.data:
            print("The employee does not exist.")
            return False
        elif employee_id in self.data:
            return True
    def save(self):
        output_file=open('EmployDb.dat', 'wb')
        pickle.dump(self.data, output_file)
        output_file.close()