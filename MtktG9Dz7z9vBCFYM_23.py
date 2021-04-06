
import socket
def get_domain(ip):
  return socket.gethostbyaddr(ip)[0]

