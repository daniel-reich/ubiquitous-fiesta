
def sum_round(num):
    s = str(num)
    ln = len(s) - 1
    lst = []
    for i in s:
        if i != '0':
            lst.append(i + ln*'0')
        ln = ln - 1
    return ' '.join(lst[::-1])

