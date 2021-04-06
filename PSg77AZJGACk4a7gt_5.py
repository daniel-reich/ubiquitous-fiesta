
def meme_sum(a, b):
    a_str, b_str = str(a), str(b)
    width = len(a_str) if len(a_str) > len(b_str) else len(b_str)
    a_str, b_str = a_str.zfill(width), b_str.zfill(width)
    sum_str = ''.join(str(int(dd[0]) + int(dd[1])) for dd in zip(a_str, b_str))
    return int(sum_str)

