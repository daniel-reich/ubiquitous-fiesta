
def compare_data(*args):
    if len(args) == 0 or len(args) == 1:
        return True
    else:
        type_args = type(args[0])
        for item in args:
            if type(item) != type_args:
                return False
        return True

