
def convert_base(n, base):
    b = 0
    b_list = []
    while True:
        power = base**b
        b += 1
        b_list.append(power)
        if power > n:
            break
    b_list.sort(reverse=True)
​
    answer = ''
    for i in b_list:
        x = n // i
        answer += str(x)
        if x > 0:
            n -= i*x
    return int(answer)
​
​
def is_Esthetic(n):
    c = 0
    n = str(n)
    for i in range(len(str(n))-1):
        if abs(int(n[i]) - int(n[i + 1])) == 1:
            c += 1
    if c == len(str(n))-1:
        return True
​
def esthetic(n):
    list_of_bases = []
    for i in range(2, 11):
        all_bases = convert_base(n, i)
        if is_Esthetic(all_bases):
            list_of_bases.append(i)
    if len(list_of_bases) > 0:
        return list_of_bases
    else:
        return 'Anti-Esthetic'

