
import socket
def get_domain(ip_address):
  return socket.gethostbyaddr('8.8.8.8')[0]

