import socket
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
sock.bind((UDP_IP, UDP_PORT))

try:
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print(f"Received message: {data} from {addr}")
        sock.sendto(b"Response from server", addr)  # Send response to the same port
except KeyboardInterrupt:
    sock.close()
    sys.exit(0)
