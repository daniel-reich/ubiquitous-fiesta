
def forbidden_letter(char, lst):
    return len([i for i in lst if char in i])==0

