
def get_domain(ip_address):
  from socket import gethostbyaddr
  return gethostbyaddr(ip_address)[0]

