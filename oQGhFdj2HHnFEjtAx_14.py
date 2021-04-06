
def slicer(string, slic):
    # simple cases:
    if slic == string:
        return "[:]"
    if slic == string[::-1]:
        return "[::-1]"
    if slic == string[0]:
        return "[0]"
    n = len(slic)
    m = len(string)
    if slic == string[:n]:
        return "[:" + str(n) + "]"
    if slic == string[-n:]:
        return "[-" + str(n) + ":]"
    if slic in string:
        idx = string.find(slic)
        return "[" + str(idx) + ":" + str(idx + n) + "]"
    # "forward" cases:
    for start in range(m - 1):
        delta = 2
        while True:
            if start + delta * (n - 1) >= m:
                break
            s_slice = ''.join([string[start+k*delta] for k in range(n)])
            if s_slice == slic:
                ans = "["
                if start > 0 :
                    ans += str(start)
                ans += ":"
                end = start + delta * (n - 1)
                if end + delta < m:
                    ans += str(end + 1) 
                ans += ":" + str(delta) + "]"
                return ans
            delta += 1
    # "reverse" cases:
    for start in range(m - 1, 0, -1):
        delta = -1
        while True:
            if start + delta * (n - 1) < 0:
                break
            s_slice = ''.join([string[start+k*delta] for k in range(n)])
            if s_slice == slic:
                ans = "[" 
                if start < m - 1:
                    ans += str(start)
                ans += ":"
                end = start + delta * n
                if end >= 0:
                    ans += str(end)
                ans += ":" + str(delta) + "]"
                return ans
            delta -= 1

