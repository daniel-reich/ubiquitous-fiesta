
def number_of_repeats(s):
    strlen = len(s)
    sublen = 2
    while True:
        if len(s) % sublen == 0:
            m = len(s) // sublen
            if s == s[:sublen] * m:
                return m
        sublen += 1

