
def compare_data(*args):
    for i in list(args):
        for j in list(args):
            if type(i)!=type(j):
                return False
    return True

