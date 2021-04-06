
def license_plate(s, n):
    s = s.upper().replace('-', '')[::-1]
    return '-'.join(s[i:i+n] for i in range(0, len(s), n))[::-1]

