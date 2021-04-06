
import socket
def get_domain(ip_address):
  return socket.getnameinfo((ip_address, 0), 0)[0]

