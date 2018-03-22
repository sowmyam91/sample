from BaseHTTPServer import BaseHTTPRequestHandler
import re
from handler import get_employee, get_employees


class EmployeeHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        emp_grp = re.match(r'(\/employees\/(\d+)\/?$)', self.path)
        emps_grp = re.match(r'(\/employees\/?$)', self.path)

        if emp_grp:
            print emp_grp
            emp_id = emp_grp.group(2)
            response = get_employee(emp_id)
            self.send_response(200)
        elif emps_grp:
            response = get_employees()
            self.send_response(200)
        else:
            self.send_response(400)
            response = {"mesage": "BAD Request"}
        self.end_headers()
        self.wfile.write(response)
        return

    def do_POST(self):
        pass

    def do_DELETE(self,):
        pass

    def do_UPDATE(self):
        pass

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer

    server = HTTPServer(('localhost', 8000), EmployeeHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()