
def missing_alphabets(s):
    max_freq = 0
    for i in range(97, 123):
        chr_i = chr(i)
        if chr_i in s:
            freq = s.count(chr_i)
            if freq > max_freq:
                max_freq = freq
    res = ""
    for i in range(97, 123):
        chr_i = chr(i)
        if chr_i in s:
            freq = s.count(chr_i)
            res += chr_i * (max_freq - freq)
        else:
            res += chr_i * max_freq
    return res

