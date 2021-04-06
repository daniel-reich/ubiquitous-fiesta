
def recur_index(txt, ix = 0, best = None):
    if not txt: return {}
    if not best: best = {}
    if ix == len(txt): return best
    nx = txt.find(txt[ix], ix + 1)
    if nx >= 0:
        if not best or list(best.values())[0][1] > nx:
            best = {txt[ix]: [ix, nx]}
    return recur_index(txt, ix + 1, best)

