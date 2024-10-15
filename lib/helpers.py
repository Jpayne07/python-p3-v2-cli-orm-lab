from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    input_name = input("Please enter a name: ")
    employee = Employee.find_by_name(input_name)
    print(employee) if employee else print (f"{input_name} is not an employee at this company")



def find_employee_by_id():
    input_id = input("Please enter an employee id: ")
    employee_id = Employee.find_by_id(input_id)
    print(employee_id) if employee_id else print (f"{input_id} there is not an employee with that id at this company")


def create_employee():
    new_employee_name = input("Please enter new employee's name: ")
    new_employee_job_title = input("Please enter new employee's job title: ")
    _id = input("Please enter new employee's department id: ")
    try:
        employee = Employee.create(new_employee_name, new_employee_job_title, _id)
        print(f"{employee} added")
    except Exception as exc:
        print("Error updating department: ", exc)
        

    
    # print(new_employee)


def update_employee():
    _id = input("enter an employee id: ")
    employee = Employee.find_by_id(_id)
    if employee:
        try:
            _name = input("Enter name: ")
            employee.name = _name
            _job_title = input("Enter job: ")
            employee.job_title = _job_title
            _department_id = input("Enter new department id: ")
            employee.department_id = _department_id
            employee.update()
            print(f"Success! Employee: {_name} with title {_job_title} and department id = {_department_id} updated")
        except Exception as exc:
            print('Error Updating: ', exc)


def delete_employee():
    _id = input("Enter employee's id: ")
    del_employee = Employee.find_by_id(_id)
    if del_employee:
        del_employee.delete()
        print(f"deleted employee {del_employee}")
    else:
        print("employee not found")

def list_department_employees():
    dep_id = input("Enter the department id: ")
    department = Department.find_by_id(dep_id)
    if department:
        for employee in department.employees():
            print(employee)
    else:
        print("department does not exist")