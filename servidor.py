import socket
from pathlib import Path
from utils import extract_route,read_file,build_response
from views import *

CUR_DIR = Path(__file__).parent
SERVER_HOST = 'localhost'
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind((SERVER_HOST,SERVER_PORT))
server_socket.listen()

print(f"f'Servidor escutando em (ctrl+click): http://{SERVER_HOST}:{SERVER_PORT}'")

while True:
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()
    print('*'*100)
    print(request)

    route = extract_route(request)
    path = CUR_DIR / route

    print("Route: ")
    print(route)

    print("Path: ")
    print(path)

    if path.is_file():
        if path.suffix == '.css':
            response = build_response(headers='Content-Type: text/css; charset=utf-8') + read_file(path)
        else:
            response = build_response() + read_file(path)
    elif route == '':
        response = index(request)
    elif route[0:6] == ('delete'):
        response = delete(request)
    elif route[0:4] == ('edit'):
        response = edit(request)
    elif route[0:6] == ('update'):
        response = update(request)
    else:
        response = not_found(request)
    

    client_connection.sendall(response)
    client_connection.close()
server_socket.close()