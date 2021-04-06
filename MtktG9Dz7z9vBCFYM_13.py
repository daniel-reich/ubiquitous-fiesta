
import socket
def get_domain(ip_address):
  req = socket.gethostbyaddr(ip_address)
  return req[0]

