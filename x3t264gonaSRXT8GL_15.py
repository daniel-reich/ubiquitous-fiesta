
def repeating_cycle(denr):
 
    res = ""
    mp = {}
    rem = 1 % denr
​
    while ((rem != 0) and (rem not in mp)):
        mp[rem] = len(res)
        rem = rem * 10
        res_part = rem // denr
        res += str(res_part)
        rem = rem % denr
    
​
    if len(res) > len(res[mp[rem]:]):
        return -1
​
    return len(res[mp[rem]:])

