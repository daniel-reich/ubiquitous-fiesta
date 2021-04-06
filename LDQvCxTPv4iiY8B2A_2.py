
def same_upsidedown(s):
    return s[::-1] == s.translate(s.maketrans('69', '96'))

