
def look_and_say(start, n):
    if n == 1:
        return [int(start)]
    lis = []
    cur = ''
    for i in str(start):
        if (not cur) or cur[0] == i:
            cur += i
        else:
            lis.append(cur)
            cur = i
    lis.append(cur)
    nec = ''
    for i in lis:
        if i:
            nec += str(len(i)) + str(i[0])
    return [int(start)] + look_and_say(nec, n-1)

