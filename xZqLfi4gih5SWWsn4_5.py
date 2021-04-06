
def license_plate(code, group):
    output = []
    return '-'.join(license(''.join([x for x in code if x != '-']), group, output))
​
def license(code, group, combined):
    if len(code) > group:
        combined.insert(0,code[-1*group:].upper())
        return license(code[:-1*group], group, combined)
    else:
        combined.insert(0,code.upper())
        return combined

