
def measure_the_depth(lst):
    cnt = 1
    while len(lst) > 0 and type(lst) == list:
        cnt += 1
        lst = lst[0]
    return cnt

