import socket

payload = 'Hello Python_101'
payload_bytes = payload.encode("ISO-8859-1")


content_string = len(payload_bytes)

request = (
        "POST / HTTP/1.1\r\n"
        "Host: example.com\r\n"
        "Content-Type: text/plain\r\n"
        f"Content-Length: {content_string}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{payload}"
)

s= socket.socket()

s.connect(("localhost", 28333))

s.sendall(request.encode("ISO-8859-1"))

request_bytes = b""


while True: 
    data = s.recv(4096)
    if len(data) == 0 :
        break
    request_bytes += data 


s.close()

print(request_bytes.decode("ISO-8859-1"))


