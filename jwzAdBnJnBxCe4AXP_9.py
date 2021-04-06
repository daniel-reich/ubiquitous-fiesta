
def rearranged_difference(num):
    return int("".join(sorted(str(num),reverse=True)))-int("".join(sorted(str(num))))

