
def hamming_distance(txt1, txt2):
    return len([1 for ch1, ch2 in zip(txt1, txt2) if ch1 != ch2])

