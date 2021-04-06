
def valid_str_number(n):
    if n.count(".") > 1:
        return False
    for i in n:
        if i.isalpha():
            return False
    return True

