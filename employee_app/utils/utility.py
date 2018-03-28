from template_handler.jinja_handler import convert_response


def validate_user(func_api):
    """
    Decorator verifies the user creds.
    Modifies the response to XML.
    :param func_api:
    :return: XML response
    """
    def verify_creds(self, *args, **kwargs):

        if self.headers.get('username') == "sowmya" and \
                        self.headers.get('password') == "pass123":
            response = func_api(self, *args, **kwargs)

            if response is None:
                self.send_response(400)
                response = {"status": False, "message": "BAD Request", "code": 400}
        else:
            response = {"status": False, "message": "Invalid Creds", "code": 400}
            self.send_response(400)

        if isinstance(response, dict):
            response.update(method=self.command)

        response = convert_response("templates/format_response", type='xml', data=response)

        self.end_headers()
        self.send_header("Content-type", 'text/xml')
        self.wfile.write(response)
        return
    return verify_creds
