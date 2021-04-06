
def seven_boom(lst):
    for item in lst:
        if "7" in str(item):
            return "Boom!"
    else:
        return "there is no 7 in the list"

