
def max_collatz(num):
    arr = [num]
    while arr[-1] != 1:
        if not arr[-1] % 2:
            arr.append(arr[-1] // 2)
        else:
            arr.append((arr[-1] * 3) + 1)
​
    return max(arr)

