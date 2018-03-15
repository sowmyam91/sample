from BaseHTTPServer import BaseHTTPRequestHandler
from urlparse import parse_qs, urlparse

from handler import get_employee, get_employees


class EmployeeHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        emp_id = None
        parsed_path = urlparse(self.path)

        if parsed_path.query:
            q_p = '?'+parsed_path.query
            try:
                emp_id = parse_qs(parsed_path.query).get('id')[0]
            except:
                print "Invalid query param"
            if emp_id:
                if self.path == "/employee/"+q_p:
                    response = get_employee(emp_id)
                    self.send_response(200)
                    self.end_headers()
            else:
                self.send_response(400)
                response = {"mesage": "BAD Request"}
        else:
            if self.path == "/employees/":
                response = get_employees()
                self.send_response(200)
                self.end_headers()

        # self.send_header('Content-type', 'text/json')
        self.wfile.write(response)
        return

    def do_POST(self):
        pass

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer

    server = HTTPServer(('localhost', 8000), EmployeeHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()