
def gcd(a,b):
    return gcd(b, a%b) if b else a
​
def division(a, b):
    verify = b
    while not(verify % 5): verify //= 5
    while not(verify % 2): verify //= 2
    if verify == 1:
        w = str(a / b); e, p_ = w.find("e"), w.find(".")
        p = len(w[p_+1:e]) if p_ != -1 else 0
        return str(a / b) if e == -1 else "0."+(int(w[e+2:])-1)*"0"+w[:p]+w[p+1:e]
    else:
        fit, r, p = a//b, 10*(a % b), 1; resp, w, d = str(fit)+".", "", {r//10:0}
        while True:
            if r > b:
                w += str(r//b); r = r%b
                if r % b in d: break
                d[r] = p; r *= 10; p += 1
            else: d[r], r, w, p = p, r*10, w+"0", p+1
        return resp+w[:d[r]]+"("+w[d[r]:]+")"

