import socket

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Returns 0 if the connection is successful (meaning the port is BUSY)
        return s.connect_ex(('localhost', port)) == 0

port_to_check = 8000
if is_port_in_use(port_to_check):
    print(f"Port {port_to_check} is ACTIVE (Server is likely running).")
else:
    print(f"Port {port_to_check} is FREE.")