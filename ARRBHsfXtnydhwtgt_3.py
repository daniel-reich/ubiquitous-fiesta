
from re import match
def compress(c, res=None):
    if res is None:
        res = []
        c = "".join(c)
    m = match(r"(\w)\1*", c).group()
    len_m = len(m)
    res.append(m[0])
    if len_m > 1:
        res.append(str(len_m))
    c = c[len_m:]
    return compress(c, res) if c else "".join(res)

