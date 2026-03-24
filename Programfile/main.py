from EmployDbHandler import EmployDbHandler
from AddEmployee import AddEmployee
from ListAllEmployee import ListAllEmployee
from LookUpEmployee import LookUpEmployee
from DelEmployee import DelEmployee

def main():
    db_handler=EmployDbHandler()
    command_dict={'1':AddEmployee(db_handler),'2':ListAllEmployee(db_handler),
              '3':LookUpEmployee(db_handler) ,'4':DelEmployee(db_handler)}
    try:
        while True:
            print("--------- Menu ---------")
            print("1. Add a new employee ")
            print("2. List all ")
            print("3. Look up a employee")
            print("4. Delete a employee")
            print("0. Quit the program ")
        
            choice=str(input("Enter your choice "))
            if choice == '0':
                break
            else:
                command_dict[choice].execute()
                db_handler.save()
    except :
        print("ERROR.")
        main()
main()
