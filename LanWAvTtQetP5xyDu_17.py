
def can_div(lst, n, x, y, z, lookup):
    if x + y + z == 0: return True
    if n < 0: return False
​
    key = (x, y, z, n)
    if key not in lookup:
        xin = False if x < lst[n] else can_div(lst, n-1, x-lst[n], y, z, lookup)
        yin = False if xin or y < lst[n] else can_div(lst, n-1, x, y-lst[n], z, lookup)
        zin = False if xin or yin or z < lst[n] else can_div(lst, n-1, x, y, z-lst[n], lookup)
        lookup[key] =  xin or yin or zin
    return lookup[key]
​
def coins_div(lst):
    total = sum(lst)
    share = total // 3
    if len(lst) < 3 or share * 3 != total: return False
    return can_div(lst, len(lst)-1, share, share, share, {})

