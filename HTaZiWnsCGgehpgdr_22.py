
def license_plate(s, n):
    plain = ''.join(i.upper() for i in s[::-1] if i != '-')
    chunks = [plain[i:i+n] for i in range(0,len(plain),n)]
    return '-'.join(reversed([i[::-1] for i in chunks]))

