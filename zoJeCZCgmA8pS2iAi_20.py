
def count_func_call(f):
    if type(f).__name__ == 'function':
        return 1 + count_func_call(f())
    else:
        return 0
​
def func_sort(lst):
    return sorted(lst, key=count_func_call)

