
def valid_rondo(s):
    key = "BCDEFGHIJKLMNOPQRSTUVWXYZ"
    return s[0] == s[- 1] == "A" and s[1 : : 2] in key and len(s) > 2

