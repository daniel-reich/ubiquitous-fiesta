
def shared_digits(lst):
    for i in range(1, len(lst)):
        if len(set(str(lst[i-1])) & set(str(lst[i]))) == 0:
            return False
    return True

