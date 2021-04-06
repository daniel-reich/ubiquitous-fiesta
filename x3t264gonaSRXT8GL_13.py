
def repeating_cycle(n):
    res = ""; mp = {}; a = 1
​
    rem = a % n
​
    while ((rem != 0) and (rem not in mp)):
        mp[rem] = len(res); rem = rem * 10
        res_part = rem // n; res += str(res_part); rem = rem % n
    if res[1:] == res[mp[rem]:]:
        return -1
    return len(res[mp[rem]:])

