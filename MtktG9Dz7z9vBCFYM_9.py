
def get_domain(ip_address):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((ip_address, 80))
    s.close()
    domain = socket.gethostbyaddr(ip_address)[0]
    return domain

