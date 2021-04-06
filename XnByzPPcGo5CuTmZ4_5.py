
def kix_code(addr):
    addr = addr.split(',')
    kix = ''.join(addr[2].split()[:2])
    middle = addr[1].upper()
    idx = 0
    while True:
        if '0' <= middle[idx] <= '9':
            break
        idx += 1
    for c in middle[idx:]:
        if '0' <= c <= '9' or 'A' <= c <= 'Z':
            kix += c
        else:
            kix += 'X'
    return kix

