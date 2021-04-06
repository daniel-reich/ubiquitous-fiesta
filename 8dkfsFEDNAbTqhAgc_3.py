
def division(a, b):
    nq = []
    if a % b == 0:
        return str(a/b)
    ans = str(a // b)+chr(46)
    while a!=0:
        r = a % b
        if r == 0:
            for i in nq:
                ans += str(i[1])
            break
        a = r*10
        q = a // b
        if [a, q] in nq:
            p = nq.index([a, q])
            for i in nq[:p]:
                ans += str(i[1])
            ans += chr(40)
            for i in nq[p:]:
                ans += str(i[1])
            ans += chr(41)
            break        
        else:
            nq.append([a, q])
    return ans

