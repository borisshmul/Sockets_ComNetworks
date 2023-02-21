 # A simple TCP server. When a client connects, it sends the client the current
 # datetime, then closes the connection. This is arguably the simplest server
 # you can write. Beware though that a client has to be completely served its
 # date before the server will be able to handle another client.

import socketserver
from datetime import datetime

class DateHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.wfile.write(f'{datetime.now().isoformat()}\n'.encode('utf-8'))

with socketserver.TCPServer(('', 59090), DateHandler) as server:
    print('The date server is running...')
    server.serve_forever()
