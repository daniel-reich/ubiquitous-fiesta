
def bw_transform(text):
    bwt = [text[k:] + text[:k] for k in range(len(text))]
    bwt.sort()
    return ''.join([row[-1] for row in bwt])

