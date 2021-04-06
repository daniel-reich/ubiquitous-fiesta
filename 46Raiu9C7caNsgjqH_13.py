
def compare_data(*args):
    if args == None:return True
    for i in range(len(args)):
        if type(args[0])!=type(args[i]):
            return False
    return True

