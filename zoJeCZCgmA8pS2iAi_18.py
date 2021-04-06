
def func_sort(lst):
    def depth(f):
        res = 0
        while callable(f):
            f = f()
            res += 1
        return res
    return sorted(lst, key=depth)

