
def bw_transform(text):
    l = sorted([text[i:]+text[:i] for i in range(len(text))])
    return ''.join([i[-1] for i in l])

