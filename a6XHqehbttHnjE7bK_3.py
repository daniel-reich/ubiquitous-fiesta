
def is_repdigit(num):
    for ele in str(num):
        if ele != str(num)[0]:
            return False
            break
        else:
            continue
    return True

