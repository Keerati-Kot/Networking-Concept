import socket

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 28333))
s.listen()

while True :
    

    new_socket, client_address = s.accept()

    requests_data = b""


    ip, port = client_address
    print(f"Client connect from IP : {ip}, Port : {port}")





    while True :
        data = new_socket.recv(4096)
        if not data :
            break
        requests_data += data

        if b"\r\n\r\n" in requests_data :
            break

    requests = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        "Content-Length: 12\r\n"
        "Connection: close\r\n"
        "\r\n"
        "thiscomputer"
    )


    new_socket.sendall(requests.encode("ISO-8859-1"))

    new_socket.close()

