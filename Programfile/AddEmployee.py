import EmployeeClass

class AddEmployee:
    def __init__(self, db_handler):
        self.db_handler=db_handler
    def execute(self):
        Id=str(input("Please enter the employee ID: "))
        if self.db_handler.check_if_exist(Id) is False:
            Name=str(input("The employee name: "))
            EmployeeType=str(input("Type (1)Worker (2)Supervisor: "))
            if(EmployeeType=='1'):
                Shift=str(input("Shift (1)day (2)night: "))
                Rate = input("Rate: ")
                Object=EmployeeClass.WorkerClass(Name,Id,EmployeeType,Shift,Rate)
                self.db_handler.add_modify_employee(Object)
                print("The entry has been added.")

            elif(EmployeeType=='2'):
                Salary = input("Salary: ")
                Bonus = input("Bonus: ")
                Object=EmployeeClass.SupervisorClass(Name,Id,EmployeeType,Salary,Bonus)
                self.db_handler.add_modify_employee(Object)
                print("The entry has been added.")
                
            else:
                print('No have your choice. ')
        else:
            print("The employee exists.")
