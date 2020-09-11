from http.server import BaseHTTPRequestHandler
from urllib import parse
from project.core.LogRecord import LogRecord
from project.presenters.ConsolePresenter import ConsolePresenter


class HttpSinkHandler(BaseHTTPRequestHandler):
    presenters = None
    storages = None

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        logRecord = LogRecord.fromJson(self.rfile.read(content_len))
        self.storeRecord(logRecord)
        self.presentRecord(logRecord)
        self.send_response(200)
        self.end_headers()

    def presentRecord(self, logRecord : LogRecord):
        for presenter in self.server.presenters:
            presenter.presentLogRecord(logRecord)

    def storeRecord(self, logRecord:LogRecord):
        for storage in self.server.storages:
            storage.store(logRecord)

    """
    Turns off internal logging
    """
    def log_message(self, format, *args):
        return        

    # def do_GET(self):
    #     parsed_path = parse.urlparse(self.path)
    #     message_parts = [
    #         'CLIENT VALUES:',
    #         'client_address={} ({})'.format(
    #             self.client_address,
    #             self.address_string()),
    #         'command={}'.format(self.command),
    #         'path={}'.format(self.path),
    #         'real path={}'.format(parsed_path.path),
    #         'query={}'.format(parsed_path.query),
    #         'request_version={}'.format(self.request_version),
    #         '',
    #         'SERVER VALUES:',
    #         'server_version={}'.format(self.server_version),
    #         'sys_version={}'.format(self.sys_version),
    #         'protocol_version={}'.format(self.protocol_version),
    #         '',
    #         'HEADERS RECEIVED:',
    #     ]
    #     for name, value in sorted(self.headers.items()):
    #         message_parts.append(
    #             '{}={}'.format(name, value.rstrip())
    #         )
    #     message_parts.append('')
    #     message = '\r\n'.join(message_parts)
    #     self.send_response(200)
    #     self.send_header('Content-Type',
    #                      'text/plain; charset=utf-8')
    #     self.end_headers()
    #     self.wfile.write(message.encode('utf-8'))


class HttpSink:
    def __init__(self, presenters, storages):
        from http.server import HTTPServer
        self.server = HTTPServer(('localhost', 8080), HttpSinkHandler)
        self.server.presenters = presenters
        self.server.storages = storages


    def start(self):
        print('Starting http-sink, use <Ctrl-C> to stop')
        self.server.serve_forever()        
    
