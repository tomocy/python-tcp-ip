import http.server

HOST = "localhost"
PORT = 9000

server = http.server.HTTPServer(
    (HOST, PORT), http.server.SimpleHTTPRequestHandler
)

server.serve_forever()
