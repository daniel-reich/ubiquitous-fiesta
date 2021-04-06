
def license_plate(code, group):
    code = code.upper()
    #if length of characters excluding '-' is a multiple of group
    if len(code.replace("-",'')) % group == 0:
        #don't want to add another dash if *'s is a multiple of group
        code = '*'*(group-1) + code
    return license_plate2(code,group)
def license_plate2(code,group):
    #BASE CASE
    if code[0] == '-':
        return license_plate2(code[1:],group)
    elif len(code) == 1:
        return code
    #RECURSIVE CASE
    y = code[0] + license_plate2(code[1:],group)
    #GROUPING CODES
    if y[0] == '-' or len(y.replace("-",'')) % group != 0:
        #if length of characters in initial 
        #code excluding '-' is a multiple of group, to prevent logic error 
        if '*' in y:
            normstr = '*'*(group-1) + '-'
            return y.strip(normstr)
        return y
    elif len(y.replace("-",'')) % group == 0:
        return '-' + y

