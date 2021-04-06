
intersects =[
   [(4,6), (2,4), (5,4), (3,6)],
     [(2,0), (4,2), (3,2), (5,1)],
     [(1,0), (4,4), (0,2), (5,6)],
     [(4,0), (1,4), (5,2), (0,6)],
     [(3,0), (1,2), (2,2), (0,0)],
     [(1,6), (3,4), (0,4), (2,6)]]
​
fit_order = [2,1,5,0,3,4]
​
def fit_next_word(sln, fit_order_index, words):
    fit_order_index = (fit_order_index+1)%6
    isect_list_index = fit_order[fit_order_index]
    for cw in words:
        is_poss = True
        for i, s in enumerate(intersects[isect_list_index]):
            soln_index, isect = s
            if sln[soln_index] and sln[soln_index][isect] != cw[i*2]:
                is_poss = False
                break
        if is_poss:
            sln[isect_list_index] = cw
            fit_next_word(sln, fit_order_index, list(filter(lambda w: w != cw, words)))
            if all(w for w in sln): return
            sln[isect_list_index] = ''
    return 
​
def fit_words(words, clue):
    wix = clue[0]-1
    cix = fit_order.index(wix)
    for cw in filter(lambda w: w[3] == clue[1], words):
        sln = ['']*6
        sln[wix] = cw
        fit_next_word(sln, cix, list(filter(lambda w: w != cw, words)))
        if all(w for w in sln): return sln
    return None

