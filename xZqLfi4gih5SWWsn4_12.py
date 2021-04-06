
def license_plate(code, group, l=[]):
    code=code.replace('-','')
    if code=='':
        return '-'.join(l)
    return license_plate(code[:-group],group, [code[-group:].upper()]+l )

