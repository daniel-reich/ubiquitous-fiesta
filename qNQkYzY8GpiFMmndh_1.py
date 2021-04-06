
from functools import reduce
def join(lst):
    def join_2(left, right):
        for offset in range(min(len(left[0]), len(right)),0,-1):
            if left[0][-offset:] == right[:offset]:
                return [left[0]+right[offset:], min(left[1], offset)]
        return [left[0]+right,0]
    return reduce(join_2,[[lst[0], 99]]+lst[1:])

