import traceback
from datetime import datetime
from router import UrlRouter
from config import DEBUG
from config import SETTINGS


class Request:
    def __init__(self, wsgi_environ):
        self.init_time = datetime.now()
        self.body = wsgi_environ.get('wsgi.input')
        self.method = wsgi_environ['REQUEST_METHOD']
        self.query_string = wsgi_environ['QUERY_STRING']
        self.raw_uri = wsgi_environ['RAW_URI']
        self.server_protocol = wsgi_environ['SERVER_PROTOCOL']
        self.user_agent = wsgi_environ['HTTP_USER_AGENT']
        self.path = wsgi_environ['PATH_INFO']

    def read():
        if not self.body:
            return
        return self.body.read()


class Response:

    statuses = {
        200: 'OK',
        404: 'Not Found',
        500: 'Internal Server Error',
    }

    def __init__(self, body, status_code=200, headers=None):
        self.body = body if body else b''
        if headers is None:
            self.headers = [
                ('Content-Type', 'text/plain'),
                ('Content-Length', str(len(self.body))),
            ]
        status_message = self.statuses.get(status_code, 'Unknown')
        self.status_code = status_code
        self.status = '{0} {1}'.format(status_code, status_message)


class Application:
    def __init__(self):
        project_root = SETTINGS['project_root']
        self.router = UrlRouter(project_root)
        if DEBUG:
            self.console = Console()

    def handle_request(self, wsgi_environ):
        try:
            request = Request(wsgi_environ)
            handler = self.router.get_handler(request.path, request.method)
            if handler:
                response_data = handler(request)
                response = Response(body=response_data)
            else:
                response = Response(body=b'Page not found', status_code=404) # TODO: log to file
        except Exception:
            response = Response(body=b'Oops. Server error.', status_code=500)
            print(traceback.format_exc()) # TODO: log to file
        if DEBUG:
            self.log_response(request, response)
        return response.status, response.headers, response.body

    def log_response(self, request, response):
        colors_map = {
            200: self.console.green,
            404: self.console.yellow,
            500: self.console.red,
        }
        message = '{0} {1} - {2}'.format(request.method, request.path, response.status)
        color = colors_map.get(response.status_code, self.console.white)
        print(color(message))


class Console:
    def colorize(self, text, color):
        if type(text) == bytes:
            text = text.decode()
        return "\033[{0}m{1}\033[{2}m".format(color[0], text, color[1])

    def green(self, text):
        return self.colorize(text, (92, 0))

    def red(self, text):
        return self.colorize(text, (91, 0))

    def yellow(self, text):
        return self.colorize(text, (93, 0))

    def white(self, text):
        return self.colorize(text, (97, 0))
