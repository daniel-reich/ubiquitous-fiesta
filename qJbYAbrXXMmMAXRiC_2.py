
def variable_valid(var):
    if var[0] in '0123456789':
        return False
    for v in var:
        if v == ' ':
            return False
    return True

