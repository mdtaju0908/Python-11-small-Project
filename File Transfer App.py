import http.server
import http.server
import socketserver
PORT = 8000
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("",PORT), handler) as http:
    print ("Server running on port",PORT)
    http.serve_forever()