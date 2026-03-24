from EmployeeClass import WorkerClass, SupervisorClass
from SocketClient import ConnectServer
import pickle
host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940
Socket=ConnectServer(host,port)
class EmployDbHandler:
    def __init__(self):
        #try:
        #    datafile=open('EmployDb.dat','rb')
        #   self.data=pickle.load(datafile)
        #    datafile.close()
        #except FileNotFoundError:
        #    self.data={}
        self.command=''
        self.parameter={}
        self.rev_data={}
            
    def add_modify_employee(self,employee):
        if(employee.employee_type=='1'):
            self.parameter={'employee_type':'worker',
            'name':str(employee.name),'employee_id':str(employee.id),
            'shift':str(employee.shift),'rate':str(employee.rate),
            'salary':0,'bonus':0}
        elif(employee.employee_type=='2'):
            self.parameter={'employee_type':'supervisor',
            'name':str(employee.name),'employee_id':str(employee.id),
            'shift':0,'rate':0,
            'salary':str(employee.salary),'bonus':str(employee.bonus)}
            
        self.command='add_modify_employ'
        Socket.send_message(self.command,self.parameter)
        self.rev_data=Socket.wait_response() #debug using

    def del_employee(self, employee_id):
        self.command='del_employ'
        self.parameter={'employee_id':str(employee_id)}
        Socket.send_message(self.command,self.parameter)
        self.rev_data=Socket.wait_response() #debug using

    def look_up_employee(self, employee_id):
        self.command='look_up_employee'
        self.parameter={'employee_id':str(employee_id)}
        Socket.send_message(self.command,self.parameter)
        self.rev_data=Socket.wait_response()
        return self.rev_data['parameter']['information'] #return key_value

    def list_all_employee(self):
        self.command='list_all_employee'
        self.parameter={}
        Socket.send_message(self.command,self.parameter)
        self.rev_data=Socket.wait_response()
        return(self.rev_data['parameter']['employ_list'])

    def check_if_exist(self, employee_id):
        self.command='check_if_exist'
        self.parameter={'employee_id':str(employee_id)}
        Socket.send_message(self.command,self.parameter)
        self.rev_data=Socket.wait_response() #get json file
        return (self.rev_data['parameter']['exist_flag']) #return true or false
    
    def save(self):
        pass