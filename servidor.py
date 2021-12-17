import socket
import json

my_socket = socket.socket()
my_socket.bind(('localhost', 8089))
my_socket.listen(5)

while True:
    conexion, addr = my_socket.accept()
    print("Connection from: " + str(addr))
    filename = ''
    while True:
        data = conexion.recv(1024).decode('utf-8')
        if not data:
            break
        filename += data
    print("from connected user: " + filename)
    myfile = open(filename, "rb")
    data = myfile.read()
    words = data.split()

    frecuency = {}

    for word in words:
        count = frecuency.get(word.decode('ascii'), 0)
        frecuency[word.decode('ascii')] = count + 1

    jsonStr = json.dumps(frecuency)
    print(jsonStr)
    conexion.sendall(jsonStr.encode('utf-8'))
    conexion.close()