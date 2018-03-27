from BaseHTTPServer import BaseHTTPRequestHandler
import re
import json
from handler import get_employee, get_employees, delete_employees, add_employee


class EmployeeHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.verify_creds():
            emp_grp = re.match(r'(\/employees\/(\d+)\/?$)', self.path)
            emps_grp = re.match(r'(\/employees\/?$)', self.path)

            if emp_grp:
                emp_id = emp_grp.group(2)
                response = get_employee(emp_id)
                self.send_response(200)
            elif emps_grp:
                response = get_employees()
                self.send_response(200)
            else:
                self.send_response(400)
                response = {"mesage": "BAD Request"}
        else:
            response = {"mesage": "Invalid Creds"}
            self.send_response(400)
        self.end_headers()
        self.wfile.write(response)
        return

    def do_POST(self):
        if self.verify_creds():
            emp = re.match(r'(\/employees\/?$)', self.path)
            if emp:
                content_len = int(self.headers.getheader('content-length', 0))
                post_body = self.rfile.read(content_len)
                post_body = json.loads(post_body)
                status = add_employee(**post_body)
                response = {"status": status, "message": "Employee added successfully"}
                self.send_response(400)
            else:
                self.send_response(400)
                response = {"mesage": "BAD Request"}
        else:
            response = {"mesage": "Invalid Creds"}
            self.send_response(400)
        self.end_headers()
        self.wfile.write(response)
        return

    def do_DELETE(self,):
        if self.verify_creds():
            emp = re.match(r'(\/employees\/(\d+)\/?$)', self.path)
            if emp:
                emp_id = emp.group(2)
                status = delete_employees(emp_id)
                response = {"status": status, "message": "Deleted"}
                self.send_response(200)
            else:
                response = {"mesage": "BAD Request"}
                self.send_response(400)
        else:
            response = {"mesage": "Invalid Creds"}
            self.send_response(400)
        self.end_headers()
        self.wfile.write(response)
        return

    def do_UPDATE(self):
        pass

    def verify_creds(self):
        if self.headers.get('username') == "sowmya" and \
                        self.headers.get('password') == "pass123":
            return True
        return False

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8000), EmployeeHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()