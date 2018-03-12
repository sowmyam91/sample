import json
import os.path

# Import CherryPy global namespace
import cherrypy


class PeopleManager:
    """ Sample request handler class. """

    # Expose the index method through the web. CherryPy will never
    # publish methods that don't have the exposed attribute set to True.
    @cherrypy.expose
    def index(self):
        return 'Sample cherry-py example'

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def login(self):
        rawbody = cherrypy.request.body.read()
        body = json.loads(rawbody)
        response = {'status': 'Invalid Credentials', 'message': 'Failed'}
        if body.get('name') == 'sowmya' and body.get('password') == 'abc':
            response = {'status': 'Login Successful', 'message': 'Welcome'}
        return response

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def people(self):
        if cherrypy.request.method == "GET":
            response = [{"name": "Sowmya", "company": "ACL"},
                        {"name": "ABC1", "company": "Alten"},
                        {"name": "ABC2", "company": "Calsoft"},
                        {"name": "XYZ", "company": "Labs"},
                        ]
        else:
            response = {"status": "Bad request"}
        return response


tutconf = os.path.join(os.path.dirname(__file__), 'cherry.conf')

if __name__ == '__main__':
    cherrypy.quickstart(PeopleManager(), config=tutconf)
