
def next_letters(s):
    let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; res = 'A'; key = 'Z'; cnt = -2
    if s == '': return 'A'
    if s[-1] != 'Z': return s[:-1]+let[let.find(s[-1])+1]
    while key == 'Z' and abs(cnt) <= len(s):
        if s[cnt] == 'Z': res += 'A'; cnt += -1
        else: res += let[let.find(s[cnt])+1]; break
    return s[:cnt]+res[::-1] if abs(cnt+1) != len(s) else 'A'+s[:cnt]+res[::-1]

