
def alphanumeric_restriction(s):
    if s.isalpha():
        return True
    if s.isdigit():
        return True
    else:
        return False

