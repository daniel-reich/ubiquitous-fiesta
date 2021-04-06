
def validate_binary(b):
    if b[-1] == '0':
        if b[:-1].count('1') % 2 == 0:
            return True
        return False
    else:
        if b[:-1].count('1') % 2 == 1:
            return True
        return False

