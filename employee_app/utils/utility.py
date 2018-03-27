
def validate_user(func_api):
    def verify_creds(self, *args, **kwargs):
        if self.headers.get('username') == "sowmya" and \
                        self.headers.get('password') == "pass123":

            response = func_api(self, *args, **kwargs)
            if response is None:
                self.send_response(400)
                response = {"mesage": "BAD Request"}
        else:
            response = {"mesage": "Invalid Creds"}
            self.send_response(400)
        self.end_headers()
        self.wfile.write(response)
        return
    return verify_creds