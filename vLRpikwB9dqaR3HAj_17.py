
import re
def is_ord_sub(l, m):
    l="".join([str(x) + '\d*' for x in l])
    m="".join([str(x) for x in m])
    return any(re.findall(l, m))

