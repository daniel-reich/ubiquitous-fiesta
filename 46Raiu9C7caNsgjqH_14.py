
def compare_data(*args):
    arr = []
    for i in args:
        arr.append(type(i))
​
    return len(set(arr)) == 1 or len(args) == 0

