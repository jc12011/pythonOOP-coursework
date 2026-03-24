class EmployeeClass:
    def __init__(self,name,id,employee_type):
        self.name=name
        self.id=id
        self.employee_type=employee_type
    def __str__(self):
        return "Name: "+self.name + ", ID: "+ self.id #+ ", Employee Type: "+ self.employee_type
class WorkerClass(EmployeeClass):
    def __init__(self,name,id,employee_type,shift,rate):
        super().__init__(name,id,employee_type)
        self.shift=shift
        self.rate=rate
    def __str__(self):
        return "W- "+super().__str__()+ ", Shift: "+str(self.shift) + ", Rate: " + str(self.rate)
class SupervisorClass(EmployeeClass):
    def __init__(self,name,id,employee_type,salary,bonus):
        super().__init__(name,id,employee_type)
        self.salary=salary
        self.bonus=bonus
    def __str__(self):
        return "S- "+super().__str__()+", Salary: "+str(self.salary)+", Bonus: "+ str(self.bonus)