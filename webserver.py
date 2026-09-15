import socket

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 28333))
s.listen()

while True :
    
    new_socket, client_address = s.accept() 
    ip, port = client_address
    print(f"Client connect from IP : {ip}, Port : {port}")

    requests_data = b""
    Content_length = 0
    header_end = False
    
    while True :
        data = new_socket.recv(4096)
        if not data :
            break
        requests_data += data

        if not header_end and b"\r\n\r\n" in requests_data :
            header_end = True

            request_str = requests_data.decode("ISO-8859-1")
            header_part = request_str.split("\r\n\r\n")[0]

            for line in header_part.split("\r\n"):
                if line.lower().startswith("content-length:"):
                    Content_length = int(line.split(":")[1].strip())

        if header_end:
            body_bytes = requests_data.split(b"\r\n\r\n", 1)[1]
            if len(body_bytes) >= Content_length :
                break


    request_str = requests_data.decode("ISO-8859-1")
    first_line = request_str.split("\r\n")[0]
    method = first_line.split(" ")[0]
    print(f"Method : {method}")


    parts = request_str.split("\r\n\r\n")
    body_part = parts[1] if len(parts) > 1 else ""
    payload_received = body_part[:Content_length]
    print(f"Received Payload ({Content_length} bytes): {payload_received}")


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

