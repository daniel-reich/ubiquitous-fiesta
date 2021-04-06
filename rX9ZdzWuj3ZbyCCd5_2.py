
def multiply_by_11(s, rem=0, res=None):
    if res is None:
        s = s[::-1]
        res = s[0]
    rem, ans = (divmod(int(s[0]) + int(s[1]) + rem, 10) if len(s) > 1 else
                divmod(int(s[0]) + rem, 10))
    res += str(ans)
    return (multiply_by_11(s[1:], rem, res) if len(s) > 1 else
            (res + (str(rem) if rem else ""))[::-1])

