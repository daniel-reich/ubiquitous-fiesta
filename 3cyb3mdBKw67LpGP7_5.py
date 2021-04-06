
from re import findall
def numbers_need_friends_too(n):
    return int("".join("".join(m) if len("".join(m)) > 1 else "".join(m) * 3
                       for m in findall(r"(\d)(\1*)", str(n))))

