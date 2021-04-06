
def check(s, k):
    cur = int(s[:k])
    s = s[k:]
    while True:
        if len(s) == 0:
            return True
        cur += 1
        cur_s = str(cur)
        n = len(cur_s)
        if len(s) < n or s[:n] != cur_s:
            return False
        s = s[n:]       
​
def separate_numbers(s):
    n = len(s)
    for k in range(1, n - 1):
        if check(s, k):
            return "YES " + s[:k]
    return "NO"

