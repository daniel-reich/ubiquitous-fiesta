
def rotate_transform(lst, num):
    if num < 0:
        num += 4
        return rotate_transform(lst, num)
    elif num == 0:
        return [list(i) for i in lst]
    else:
        return rotate_transform(list(zip(*lst[::-1])), num-1)

