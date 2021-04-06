
def palindromic_date(string):
    d = string.split("/")
    w = d[1] + d[0] + d[2]
    if "".join(d) == "".join(d)[::-1] and w == w[::-1]:
        return True
    return False

