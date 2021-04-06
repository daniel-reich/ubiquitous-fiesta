
def bw_transform(text):
    bwt = sorted(text[i:] + text[0:i] for i in range(len(text)))
    return ''.join(col[-1] for col in bwt)

