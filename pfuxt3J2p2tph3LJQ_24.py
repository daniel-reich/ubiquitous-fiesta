
def forbidden_letter(char, lst):
    if len(lst) == 0:
        return True
​
    for i in lst:
        if char in i:
            return False
    return True

