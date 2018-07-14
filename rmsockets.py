import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        #print "{} wrote:".format(self.client_address[0])
        print (self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 7700
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
