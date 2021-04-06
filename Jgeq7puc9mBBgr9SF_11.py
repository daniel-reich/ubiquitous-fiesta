
def complete_binary(s): #w/o built-in
    def l(st):
        c = 0
        while st:
            c += 1
            st = st[1:]
        return c
    s = s[::-1]
    while l(s) % 8:
        s += "0"
    return s[::-1]

