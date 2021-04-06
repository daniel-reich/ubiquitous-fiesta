
def license_plate(code, group,s = 1):
    if len(code) <= group:
        return code
    if s:
        code = code.replace('-','').upper()
    return license_plate(code[:-group], group,0) + '-' + code[-group:]

