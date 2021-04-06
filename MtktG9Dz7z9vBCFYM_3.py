
def get_domain(ip_address):
  import socket
  a=socket.gethostbyaddr(ip_address)
  return list(a)[0]

