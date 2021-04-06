
def alpha_range(start, stop, step = 1):
    if step > 26 or step < -26 or step == 0:
        return 'step must be a non-zero value between -26 and 26, exclusive'
    if start.isupper() != stop.isupper() or start.islower() != stop.islower():
        return 'both start and stop must share the same case'
    a,b = sorted([ord(start),ord(stop)])
    if step > 0 :
        ans = [chr(i) for i in range(a,b + 1,step)]
    if step < 0:
            ans = [chr(i) for i in range(b,a - 1,step)]
    return ans

