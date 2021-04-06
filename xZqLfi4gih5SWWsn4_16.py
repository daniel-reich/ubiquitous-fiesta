
def license_plate(s, n):
    s=s.replace('-','').upper()[::-1]
    return '-'.join([s[i:i+n]for i in range(0,len(s),n)])[::-1]

