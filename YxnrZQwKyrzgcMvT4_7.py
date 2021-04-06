
def rotate_transform(lst, num):
    for i in range(num % 4):
        lst = [list(i) for i in zip(*lst[::-1])]
    return lst

