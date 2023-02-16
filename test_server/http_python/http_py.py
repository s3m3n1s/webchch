# from http.server import HTTPServer, BaseHTTPRequestHandler
#
#
# def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
#     server_address = ('127.0.0.1', 8080)
#     httpd = server_class(server_address, handler_class)
#     httpd.serve_forever()
#
#
# if __name__ == "__main__":
#     run()

from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # определяем метод `do_GET`
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')


httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()
