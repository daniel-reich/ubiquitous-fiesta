
def func_sort(lst):
    def calls(i):
        j = 0
        while True:
            if callable(i):
                j += 1
                i = i()
            else:
                return j
​
    return sorted(lst, key=calls)

