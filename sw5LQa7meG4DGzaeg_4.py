
# left blank for unlimited creativity !!
def multiply(lst):
    def a(x):
        for i, val in enumerate(lst):
            lst[i] = val * x
        return lst
    return a

