
import re
def join(lst):
    res, minsh = lst[0], 10**5
    for i in range(1, len(lst)):
        m = re.search(r'(\w+) \1', res + ' ' + lst[i])
        if m:
            ol = len(m.group(1))
            res += lst[i][ol:]
            if ol < minsh: 
                minsh = ol
        else:
            res += lst[i]
            minsh = 0
    return [res, minsh]

