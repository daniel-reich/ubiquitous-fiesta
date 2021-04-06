
def is_untouchable(n):
    if n < 2:
        return "Invalid Input"
    else:
        p_div = []
        s = 0
        for i in range(2, n**2 + 1):
            s = sum(divisors(i))
            if s == n:
                p_div.append(i)
            s = 0
        if not p_div:
            return True
        else: return p_div
​
def divisors(i):
    s = {1}
    for j in range(2, int(i**0.5)+1):
        if not i % j:
            s.add(j)
            s.add(i // j)
    return sorted(s)

