
import socket
def get_domain(ip_address):
  hostname = socket.gethostbyaddr(ip_address)
  return hostname[0]

