
def bw_transform(text):
    bwm = [text]
    for _ in range(1, len(text)):
        bwm.append(bwm[-1][1:] + bwm[-1][:1])
    return ''.join(w[-1] for w in sorted(bwm))

