
def shuffle_count(n):
    arr = list(range(1, n + 1))
    size = len(arr)//2
    target = arr
    shuffles = 0
​
    while True:
        new = []
        for i in range(size):
            new += [arr[i], arr[i+size]]
        shuffles += 1
        if new == target:
            return shuffles
        arr = new

