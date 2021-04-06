
import re
def is_there_consecutive(lst, n, times):
    if n not in lst and times == 0:
        return True
    elif n in lst and times == 0:
        return False
    else:
        SEARCH = str([n for i in range(times)])
        P = re.compile(r"{}".format(SEARCH[1:-1]))
        x = re.findall(P,str(lst))
        if len(x) == 1:
            return True
        return False

