
import socket
def get_domain(ip_address):
  return list(socket.gethostbyaddr(ip_address))[0]

