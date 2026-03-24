class ChangeEmployee:
    def __init__(self,db_handler):
        self.db_handler=db_handler
    def execute(self):
        employee_id=str(input('Enter an employee ID: '))
        if self.db_handler.check_if_exist(employee_id) is True:
            employee=self.db_handler.look_up_employee(employee_id)

            if ((employee.employee_type) == '1'):
                print("Current name is "+ employee.name,end="")
                employee.name = input(", enter a new name: ")
                print("Current shift is "+ employee.shift,end="")
                employee.shift = input(", new shift: ")
                print("Current rate is "+ employee.rate,end="")
                employee.rate = input(", new rate: ")
                self.db_handler.add_modify_employee(employee)
               

            elif ((employee.employee_type) =='2'):
                print("Current name is "+ employee.name,end="")
                employee.name = input(", enter a new name: ")
                print("Current salary is "+ employee.salary,end="")
                employee.salary = input(", new salary: ")
                print("Current bonus is "+ employee.bonus,end="")
                employee.bonus = input(", new bonus: ")
                self.db_handler.add_modify_employee(employee)
        else:
            print("The employee does not exist.")
               
            