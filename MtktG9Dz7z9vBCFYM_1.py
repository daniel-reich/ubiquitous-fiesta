
import socket as sk
def get_domain(ip_address):
  return sk.getfqdn(sk.gethostbyaddr(ip_address)[0])

