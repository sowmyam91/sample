from database_manager.employee_db import Employee
from template_handler.jinja_handler import convert_response


def get_employees():
    try:
        data = Employee().get_employees()
        return convert_response('templates/employees_detail', employees=data)
    except Exception as e:
        print e
        return None


def get_employee(emp_id):
    try:
        data = Employee().get_employee(emp_id)
        return convert_response('templates/employee_details', data=data)
    except Exception as e:
        print e
        return None

