
def max_score(s):
    one = s.count('1')
    zero = 0
    total = 0
    for i in s[:-1]:
        if i == '0':
            zero += 1 
        if i == '1':
            one -= 1
        total = max(total,zero + one)
    return total

