
def bw_transform(text):
    bw_rot =  [''.join(list(text)[i: len(text) + i] + list(text)[:i]) for i in range(len(text))]
    bw_srt = sorted(bw_rot)
    return ''.join([a[-1] for a in bw_srt])

