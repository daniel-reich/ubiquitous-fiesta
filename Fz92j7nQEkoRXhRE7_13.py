
def jumping_frog(n, s):
    p = s[0]; c = 2
    while p <= n-1:
        if s[p] == 0:
            return 'no chance :-('
        else:
            if p + s[p] == n-1:
                return c + 2
            elif p + s[p] > n-1:
                return c + 1
            else:
                if p + s[p] + s[p+s[p]] >= p - s[p] + s[p-s[p]]:
                    c += 2
                    p += s[p] + s[p+s[p]]
                else:
                    c += 2
                    p += (-s[p] + s[p-s[p]])
    else: 
        return c

