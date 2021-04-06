
def numbers_need_friends_too(n):
    n = str(n)
    i, j, size = 0, 1, len(n)
    new_n = ''
​
    while i < size:
        while j < size and n[i] == n[j]:
            j += 1
        if j - i > 1:
            new_n += n[i:j]
        else:
            new_n += n[i]*3  # lonely number
        i = j
        j += 1
​
    return int(new_n)

