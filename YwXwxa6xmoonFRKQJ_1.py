
def josephus(n):
    if n == 0:
        return False
    arr = list(range(n))
    while len(arr) > 1:
        arr.append(arr.pop(0))
        arr = arr[1:]    
    return arr.pop()

