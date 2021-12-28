# Librairies
import http.server

# Paramétrage du serveur Web
PORT = 8888
server_address = ("", PORT)
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

print("Serveur actif sur le port :", PORT)
httpd = server(server_address, handler)

httpd.serve_forever()
