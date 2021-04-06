
from re import match
def secret(s):
    m = match(r"(\w+)>(\w+)\.(\w+)([$]+)\*(\d)", s)
    return ("<{0}>{1}</{0}>"
            .format(m.group(1),
                    "".join("<{0} class=\'{1}{2}{3}\'></{0}>"
                            .format(m.group(2), m.group(3),
                                    "0" * (len(m.group(4)) - 1), i)
                            for i in range(1, int(m.group(5)) + 1))))

