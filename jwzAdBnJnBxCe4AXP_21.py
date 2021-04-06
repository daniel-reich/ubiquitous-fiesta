
def rearranged_difference(num):
    num=str(num)
    return int(''.join(sorted(num, reverse=True)))-int(''.join(sorted(num)))

