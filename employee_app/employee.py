from BaseHTTPServer import BaseHTTPRequestHandler
import re
import json
from handler import get_employee, get_employees, delete_employees, add_employee
from utils.utility import validate_user


class EmployeeHandler(BaseHTTPRequestHandler):
    @validate_user
    def do_GET(self):
        response = None
        status = True
        code = 200
        message = "Data exists"
        emp_grp = re.match(r'(\/employees\/(\d+)\/?$)', self.path)
        emps_grp = re.match(r'(\/employees\/?$)', self.path)

        if emp_grp:
            emp_id = emp_grp.group(2)
            response = get_employee(emp_id)
        elif emps_grp:
            response = get_employees()

        if not response:
            status = False
            code = 400
            message = "Bad request"
        self.send_response(code)
        return {"data": response, "status": status, "code": code, "message": message}

    @validate_user
    def do_POST(self):
        response = None
        emp = re.match(r'(\/employees\/?$)', self.path)

        if emp:
            code = 200
            content_len = int(self.headers.getheader('content-length', 0))
            post_body = self.rfile.read(content_len)
            post_body = json.loads(post_body)
            status, err = add_employee(**post_body)

            if status:
                response = {"status": status, "message": "Employee added successfully", "code": code}
            else:
                code = 409
                response = {"status": status, "message": err.message, "code": code}
            self.send_response(code)
        return response

    @validate_user
    def do_DELETE(self, ):
        response = None
        code = 200
        emp = re.match(r'(\/employees\/(\d+)\/?$)', self.path)

        if emp:
            emp_id = emp.group(2)
            status = delete_employees(emp_id)
            if not status:
                code = 404
                response = {"status": status, "message": "Employee ID Not found", "code": code}
            else:
                response = {"status": status, "message": "Deleted", "code": code}
            self.send_response(code)

        return response

    def do_UPDATE(self):
        pass


if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer

    server = HTTPServer(('localhost', 8000), EmployeeHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
