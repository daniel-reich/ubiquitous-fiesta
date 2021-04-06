
def two_product(arr, N):
    uniqnum = set()
    for num in arr:
        if N % num == 0 and (N/num) in uniqnum:
            return [N/num, num]
        uniqnum.add(num)
    return

