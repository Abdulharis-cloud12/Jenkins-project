import socket
host = 'www.facebook.com'

try:
    addr = socket.gethostbyname(host)
    print(addr)
    
except socket.gaierror:
    print("The website was not found")