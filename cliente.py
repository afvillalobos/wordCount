import socket, sys, json, string
from dataclasses import replace

### se establece conexión con servidor ###
my_socket = socket.socket()
my_socket.connect(('localhost', 8089))

### se lee nombre archivo
Filename = sys.argv[1]

### se envía archivo a servidor para ser procesado
my_socket.send(Filename.encode('utf-8'))
my_socket.shutdown(socket.SHUT_WR)

### Se recibe json con palabras contadas
data = my_socket.recv(1024).decode('utf-8')
a = data.split(",")

### se imprime conteo de palabras
for i in a:
    print(str(i).replace("{", "").replace("}", "").replace(":", "").replace("\"", ""))

my_socket.close()