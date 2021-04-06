
def number_length(num):
    if num == 0:
        return 1
    cnt = 0
    while num > 0:
        num = num // 10
        cnt += 1
    return cnt

