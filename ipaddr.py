from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

# Set up logging
logging.basicConfig(filename='access_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Log the client's IP address
        client_ip = self.client_address[0]
        logging.info(f'Client IP: {client_ip}')

        # Respond to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Your IP address has been logged.')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
