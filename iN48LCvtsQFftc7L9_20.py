
def word_search(letters, words):
    sht, lng = min(len(w) for w in words), max(len(w) for w in words)
    words = [w.upper() for w in words]
    for i in range(len(letters)):
        wrdset = set(w for w in words if w.startswith(letters[i]))
        if wrdset:
            for dr, dc in [(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)]:
                wrd = letters[i]
                r, c = (i // 8)+dr, (i % 8)+dc
                wset = wrdset.copy()
                while 0<=r<8 and 0<=c<8 and len(wrd)<lng and len(wset)>0:
                    wrd += letters[r*8+c]
                    wset = {w for w in wset if w.startswith(wrd)}
                    if len(wrd) >= sht:
                        if wrd in wset:
                            words.remove(wrd)
                            wset.remove(wrd)
                            wrdset.remove(wrd)
                            break
                    r += dr
                    c += dc
                if len(words) == 0:
                    return True
                if not wrdset:
                    break
    return False

