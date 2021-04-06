
import socket
def get_domain(ip_address):
    return socket.getfqdn(ip_address)

