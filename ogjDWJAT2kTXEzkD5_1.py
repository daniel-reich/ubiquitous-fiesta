
def all_truthy(*args):
    my_list = []
    for i in args:
        if i:
            my_list.append(True)
        else:
            my_list.append(False)
    if False in my_list:
        return False
    else:
        return True

