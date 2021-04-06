
def numbers_need_friends_too(n):
    if len(set(str(n))) == 1:
        return n
​
    s = str(n)
    groups = []
    digits = s[0]
​
    for i in s[1:]:
        if i != digits[-1]:
            groups.append(digits)
            digits = ''
        digits += i
​
    if digits == groups[-1]:
        groups[-1] += digits
    else:
        groups.append(digits)
​
    return int(''.join(x * 3 if len(x) == 1 else x for x in groups))

