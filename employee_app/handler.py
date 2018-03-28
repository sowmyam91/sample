from database_manager.employee_db import Employee
from template_handler.jinja_handler import convert_response


def get_employees():
    try:
        data = Employee().get_employees()
        return convert_response('templates/emps_xml', type='xml', employees=data)
    except Exception as e:
        print e
        return None


def get_employee(id):
    try:
        data = Employee().get_employee(id)
        return convert_response('templates/emp_xml', type='xml', data=data)
    except Exception as e:
        print e
        return None


def delete_employees(id):
    try:
        emp = Employee().get_employee(id)
        if emp:
            return Employee().delete_employee(id)
        else:
            return False
    except Exception as e:
        print e
        return False


def add_employee(**data):
    try:
        # data = convert_response('templates/add_emp_json', type='json', data=data)
        return Employee().add_employee(**data), None
    except Exception as e:
        print e
        return False, e
