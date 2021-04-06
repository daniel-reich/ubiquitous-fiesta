
def word_search(le, w):
    sd, gr, lt, le = [i[::-1] for i in w], {}, [], le.lower(); mix = list(zip(w, sd))
    for i in range(64): gr[(int(i / 8), i - 8 * int(i / 8))] = i
    for wd in mix:
        for li in range(8):
            if any(i in le[gr[li, 0]:gr[li, 7] + 1] or i in le[gr[(0, li)]:gr[(7 - li, 7)] + 1:9]
                   or i in le[gr[li, 0]::9] or i in le[gr[li, 7]::7] or i in le[gr[0, li]:gr[7, li] + 1:8]
                   or i in le[gr[(0, 7 - li)]:gr[(7 - li, 0)] + 1:7] for i in wd): lt.append(wd[0]); break
    return True if len(lt) == len(w) else False

