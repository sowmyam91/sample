from BaseHTTPServer import BaseHTTPRequestHandler
import re
import json
from handler import get_employee, get_employees, delete_employees, add_employee
from utils.utility import validate_user


class EmployeeHandler(BaseHTTPRequestHandler):

    @validate_user
    def do_GET(self):
        response = None

        emp_grp = re.match(r'(\/employees\/(\d+)\/?$)', self.path)
        emps_grp = re.match(r'(\/employees\/?$)', self.path)

        if emp_grp:
            emp_id = emp_grp.group(2)
            response = get_employee(emp_id)
            self.send_response(200)
        elif emps_grp:
            response = get_employees()
            self.send_response(200)
        return response

    @validate_user
    def do_POST(self):
        response = None

        emp = re.match(r'(\/employees\/?$)', self.path)

        if emp:
            content_len = int(self.headers.getheader('content-length', 0))
            post_body = self.rfile.read(content_len)
            post_body = json.loads(post_body)
            status, err = add_employee(**post_body)
            print status, err
            if status:
                self.send_response(200)
                response = {"status": status, "message": "Employee added successfully"}
            else:
                self.send_response(409)
                response = {"status": status, "message": err.message }
        return response

    @validate_user
    def do_DELETE(self,):
        response = None

        emp = re.match(r'(\/employees\/(\d+)\/?$)', self.path)

        if emp:
            emp_id = emp.group(2)
            status = delete_employees(emp_id)
            if not status:
                response = {"status": status, "message": "Employee ID Not found"}
                self.send_response(404)
            else:
                response = {"status": status, "message": "Deleted"}
                self.send_response(200)

        return response

    def do_UPDATE(self):
        pass


if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8000), EmployeeHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()